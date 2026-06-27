# Replication prompt — AMI-only call webhook (paste into the new project's CLAUDE.md)

> Use this as the CLAUDE.md / task brief for a **different** PBX integration where the
> only access is an **Asterisk Manager Interface (AMI) login from an outer machine**
> (host + AMI username + secret). There is **no SSH, no filesystem access, no
> `asterisk -rx` shell, and no ability to edit PBX config files.** Everything must work
> over the AMI TCP socket alone.

## Goal
Build a long-running daemon (runs on the outer machine) that connects to the remote
Asterisk AMI and POSTs JSON to a CRM webhook for each call lifecycle stage:
`call_initiated`, `call_answered`, `call_hangup`, and (if achievable, see below)
`recording_ready`. One POST per stage per call. Every POST carries a common field set.

## Connection
- Connect TCP to `AMI_HOST:5038`; login `Action: Login` with `Username`/`Secret`.
- Request event classes you need: `Events: call,cdr,dialplan` (call → Newchannel/
  BridgeEnter/Hangup, cdr → Cdr, dialplan → VarSet for recording filename).
- Set the socket to **blocking** after connect; parse the AMI line protocol (key`: `value,
  blank line terminates an event). Reconnect with backoff on drop.
- The AMI account must be reachable from the outer machine — this means AMI is exposed on
  the network. **Security: restrict by firewall/IP allowlist and use TLS (AMI over TLS,
  port 5039) if available. Never expose AMI 5038 to the open internet in cleartext.**

## Common fields on every POST
- `direction`: `inbound` | `outbound` | `internal` | `unknown`
- `side`: tenant tag (string) or `null`
- `client_number`: external party (caller in / callee out; for internal = the called ext)
- `line_number`: our DID/line (`null` for internal)
- `ext_number`: the local extension (inbound: the answering ext; out/internal: the ext that originated)
- plus `uniqueid`, `linkedid`, `ts`, and event-specific fields.

Compute `direction`/`side`/`client_number`/`line_number` **once** at the first channel of a
call (`Newchannel`), store keyed by `linkedid`, and attach to all later events so they agree.
`ext_number` for inbound is unknown at initiation — fill it at `call_answered`.

## Event handling

### call_initiated  ← AMI `Newchannel`
- Dedupe per `Linkedid` (first channel only).
- Drop scanner/fraud calls: ignore when `Context` starts with `from-sip-external`
  (mark the linkedid ignored so later legs are dropped too).
- Classify (see rules). Store metadata. POST.

### call_answered  ← AMI `BridgeEnter`
- Real two-leg bridge = human pickup. One POST per call (dedupe per `Linkedid`).
- Extract the extension from the channel name, handling **both** forms:
  `SIP/2012-xxxx` → `2012`, and queue legs `Local/2012@from-queue-xxxx;1` → `2012`
  (take text after `/`, drop the trailing `-id`, then split on `@`).
- Bridge legs arrive in any order; for **inbound**, **hold** the POST until a leg whose
  parsed value is a known local extension appears, so `ext_number` is populated (don't let
  the trunk/Local leg fire it with a null ext).

### call_hangup
Two strategies — pick based on what the AMI account can do:
- **Preferred (rich):** if you can enable `cdr_manager.so` via `Action: Command`
  (`Command: module load cdr_manager.so`) and it emits the `Cdr` event, use it. Forward
  only the **master** record where `Cdr.UniqueID == the call's Linkedid` (queue/ring-group
  produce many CDR legs — forward one). Gives `duration`, `billsec`, `disposition`, times.
  Back-fill `ext_number` from the CDR `DestinationChannel` if still null.
- **Fallback (no config rights):** use the AMI `Hangup` event for the **root channel**
  (`Uniqueid == Linkedid`), dedupe per linkedid. Compute `duration` yourself from the
  `Newchannel`→`Hangup` time delta you tracked; include hangup `Cause`/`Cause-txt`.
  Disposition is not reliably available this way.

### recording_ready  (AMI-only is the hard part)
There is no filesystem, so you **cannot** symlink/serve the file from this machine.
- Capture the recording path from a `VarSet` event during the call where `Variable` is
  `MIXMONITOR_FILENAME` (or `CDR(recordingfile)`); store it keyed by linkedid. This needs
  the `dialplan` event class.
- Emit `recording_ready` only if the PBX itself exposes recordings over HTTP. Build the URL
  from a configured `PBX_REC_BASE` + the captured filename. If the PBX does **not** serve
  recordings, `recording_ready` is not deliverable from the outer machine — document that
  and either omit it or emit just `recording_filename` for a separate retrieval job
  (FreePBX UCP/REST, provider API, etc.).

## Classification rules (at root Newchannel)
- `Context` starts with `from-trunk`/`from-pstn` → **inbound**.
- `Context` starts with `from-internal`:
  - dialed `Exten` is a known local extension → **internal**
  - dialed `Exten` is all-digits and length ≥ `EXT_MIN_EXTERNAL` (default 6) → **outbound**
  - else (feature codes, short) → **internal**
- otherwise → **unknown**.

Party fields by direction:
| field | inbound | outbound | internal |
|-------|---------|----------|----------|
| `client_number` | `CallerIDNum` (external caller) | dialed `Exten` | dialed `Exten` |
| `line_number` | dialed `Exten` (DID) | the side's configured DID | `null` |
| `ext_number` | answering ext (from BridgeEnter) | `CallerIDNum` (originating ext) | `CallerIDNum` |

## Side / tenant tag
Config list of sides, each with `dids` (incoming numbers) and `exts` (extension list or
prefix like `"20*"`). Match inbound by **DID** (`Exten`); match outbound/internal by the
**originating extension** (`CallerIDNum`). **If multiple trunks share one gateway IP, do
not match by trunk-peer** — Asterisk tags every inbound channel with the first matching
peer; use the DID instead.

## Local extension detection (no shell)
In priority order:
1. **AMI `Command` action** (if the account has `command` privilege):
   `Action: Command` / `Command: database show AMPUSER`, parse `^/AMPUSER/(\d+)/`. Refresh
   periodically. Same data the SSH version used, just over AMI.
2. **AMI `SIPpeers`/`PJSIPShowEndpoints`** enumeration, filtering out trunk peers.
3. **Static config**: explicit extension ranges/prefixes the operator provides.

## Deliverables
- The daemon (any language; the reference impl is stdlib Python). Config block at top:
  `AMI_HOST/PORT/USER/SECRET`, `WEBHOOK_URL`, `SIDES`, `INBOUND_CTX`, `EXT_MIN_EXTERNAL`,
  extension-detection mode, optional `PBX_REC_BASE`.
- A service wrapper for the outer machine (systemd unit or equivalent) with auto-restart.
- A README documenting setup, the 4 payload schemas (with the common fields), the
  AMI-only recording caveat, and the security hardening for exposing AMI.

## Acceptance
- Inbound, outbound, and internal test calls each produce correctly-classified events with
  consistent `direction`/`side`/`client_number`/`line_number` across all stages, and
  `ext_number` populated from `call_answered` onward for answered calls.
- Exactly one POST per stage per call (queue/ring-group fan-out deduped).
- Scanner calls (`from-sip-external`) suppressed.

---

## Downstream consumer (reference: n8n `regos_create_ticket_on_call`)

This is what consumes the webhook in the original project — an **n8n** workflow that
manages a ticket in the REGOS CRM per call. Replicate the *contract*, not necessarily the
tool. The daemon's job is to feed this reliably.

### Field contract the consumer depends on
The webhook body is normalized first (n8n `call_data` code node) into:
`event`, `is_inbound = (direction.toLowerCase() == "inbound")`, `uniqueid`, `linkedid`,
`client_phone = client_number`, `line_phone = line_number`, `ext_phone = ext_number`.

Hard requirements this places on the daemon:
- **`uniqueid` must be stable and identical across all 4 events of one call** — it is the
  ticket key. The reference impl uses the master call id (`uniqueid == linkedid`).
- **`direction` must be exactly lowercase `inbound`** for the inbound branch to trigger.
- **`ext_number` must equal the agent's `internal_phone` in the CRM** — it is matched
  against the REGOS users list to find the responsible user. Wrong/empty ext → no agent
  assignment.
- `recording_ready.url` is written verbatim into a ticket field — must be publicly fetchable.

### Per-call pre-steps (run for every event before branching)
1. **Find existing ticket** for this call (sub-workflow `get_regos_ticket_data`, matched by
   `uniqueid`/`linkedid`). Tickets are linked by `external_dialog_id = "pbx:" + uniqueid`.
2. **Load all CRM users** (`User/Get`) to map `ext_phone → internal_phone → user.id`.
3. **Load channel config** (`pbx_ticket_channel` → `channel_id` for ticket creation).
4. `Switch` on `event`.

### Actions per event
- **`call_initiated`** — ensure the client exists: `client/get` by phone (Like); if none,
  `client/add` → `client_id`. Then:
  - *inbound* → create ticket (`ticket/add`, direction `Inbound`,
    `external_dialog_id=pbx:<uniqueid>`, subject `⤵️ Вход. <client> (<line>)`), **no
    responsible** yet.
  - *outbound* → resolve calling user from `ext_phone`; check `workattendance/status`. If a
    ticket already exists, set responsible + edit subject; else create ticket (direction
    `Outbound`, subject `↗️ Исход. <client> (<line>) <ext>`, `responsible_user_id =`
    attendance `Available ? <that user> : 1` fallback).
- **`call_answered`** — assign the human who picked up:
  - *inbound* → `ticket/setResponsible` to the answering ext's user, then `ticket/Edit`
    subject → `⤵️ Вход. <client> (<line>) (<ext>)`.
  - *outbound* → only if the ticket has no responsible yet: set responsible to the caller's
    user + edit subject.
- **`call_hangup`** — finalize:
  - ticket **has no responsible** (nobody handled): *inbound* → relabel subject
    `⁉️ Пропущенный.` (missed, **left open** for callback); *outbound* → `ticket/close`.
  - ticket **has a responsible**: `ticket/close`.
- **`recording_ready`** — `ticket/Edit` setting custom field `field_recording_link = url`.

### REGOS API surface used
Base `https://integration.regos.uz/gateway/out/<token>/v1/` — endpoints: `client/get`,
`client/add`, `ticket/add`, `ticket/Edit`, `ticket/setResponsible`, `ticket/close`,
`User/Get`, `workattendance/status`. (Gateway token is a secret — keep out of public repos.)

### Behavioural notes for the replica
- **Idempotency / ordering:** the consumer guards against duplicate tickets ("has existing
  ticket" check) and tolerates out-of-order events by always re-fetching the ticket by
  `uniqueid`. The daemon should still emit each stage at most once.
- The workflow inserts ~0.5s `Wait` nodes between CRM calls to let writes propagate / avoid
  races — a downstream concern, but it means the daemon need not itself debounce.
- Subject emoji convention: `⤵️ Вход.` inbound · `↗️ Исход.` outbound · `⁉️ Пропущенный.`
  missed; format `<emoji> <label>. <client> (<line>) (<ext>)`.
- "Missed" = an inbound call that hung up with no responsible assigned (never answered by an
  agent) — directly downstream of the daemon's `call_answered` never firing, which is why
  `call_answered` must fire reliably on real pickups (the ext-leg handling above).
