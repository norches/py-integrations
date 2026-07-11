from __future__ import annotations

import base64
import json
import time
from typing import Any, Dict, Optional

import httpx

from config.settings import settings as app_settings

from .config import ChatGptRegosAssistantConfig


_SENSITIVE_TOKEN_FIELDS = {"access_token", "refresh_token", "id_token"}
_PUBLIC_CLAIM_KEYS = {
    "sub",
    "user_id",
    "userid",
    "id",
    "name",
    "full_name",
    "fullname",
    "preferred_username",
    "login",
    "email",
    "phone",
    "scope",
    "exp",
}


def oauth_token_url() -> str:
    return f"{str(app_settings.oauth_endpoint or '').rstrip('/')}/oauth/token"


def oauth_client_id() -> str:
    return str(app_settings.oauth_client_id or "").strip()


def expected_origin(external_url: str) -> str:
    from urllib.parse import urlsplit

    parsed = urlsplit(str(external_url or ""))
    if not parsed.scheme or not parsed.netloc:
        return ""
    return f"{parsed.scheme}://{parsed.netloc}"


def _safe_int(value: Any, default: int) -> int:
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


def session_ttl_from_oauth_payload(payload: Dict[str, Any]) -> int:
    expires_in = _safe_int(
        payload.get("expires_in"),
        ChatGptRegosAssistantConfig.EMBED_SESSION_DEFAULT_TTL_SEC,
    )
    return max(1, min(expires_in, ChatGptRegosAssistantConfig.EMBED_SESSION_MAX_TTL_SEC))


def decode_jwt_claims(token: str) -> Dict[str, Any]:
    parts = str(token or "").split(".")
    if len(parts) < 2:
        return {}
    payload = parts[1]
    payload += "=" * (-len(payload) % 4)
    try:
        raw = base64.urlsafe_b64decode(payload.encode("ascii"))
        data = json.loads(raw.decode("utf-8"))
    except Exception:
        return {}
    return data if isinstance(data, dict) else {}


def public_claims(claims: Dict[str, Any]) -> Dict[str, Any]:
    result: Dict[str, Any] = {}
    for key, value in claims.items():
        normalized = str(key or "").lower()
        if normalized in _PUBLIC_CLAIM_KEYS and value is not None:
            result[str(key)] = value
    return result


def public_oauth_payload(payload: Dict[str, Any]) -> Dict[str, Any]:
    return {
        str(key): value
        for key, value in payload.items()
        if str(key or "").lower() not in _SENSITIVE_TOKEN_FIELDS
    }


def public_embed_session(session: Optional[Dict[str, Any]]) -> Dict[str, Any]:
    if not isinstance(session, dict):
        return {}
    oauth_payload = session.get("oauth") if isinstance(session.get("oauth"), dict) else {}
    return {
        "connected_integration_id": session.get("connected_integration_id"),
        "user": session.get("user") if isinstance(session.get("user"), dict) else {},
        "oauth": public_oauth_payload(oauth_payload),
        "created_at": session.get("created_at"),
        "expires_at": session.get("expires_at"),
    }


async def exchange_embed_token(embed_token: str) -> Dict[str, Any]:
    token = str(embed_token or "").strip()
    if not token:
        raise ValueError("embed_token is required")

    client_id = oauth_client_id()
    client_secret = str(app_settings.oauth_secret or "").strip()
    if not client_id or not client_secret:
        raise ValueError("oauth_client_id and oauth_secret must be configured")

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    form = {
        "grant_type": ChatGptRegosAssistantConfig.EMBED_TOKEN_GRANT_TYPE,
        "embed_token": token,
        "client_id": client_id,
        "client_secret": client_secret,
    }

    async with httpx.AsyncClient(timeout=30) as client:
        response = await client.post(oauth_token_url(), headers=headers, data=form)
        response.raise_for_status()
        payload = response.json()

    if not isinstance(payload, dict):
        raise ValueError("REGOS OAuth token response must be a JSON object")
    if not str(payload.get("access_token") or "").strip():
        raise ValueError("REGOS OAuth token response does not contain access_token")
    return payload


def build_embed_session(
    *,
    connected_integration_id: str,
    oauth_payload: Dict[str, Any],
    ttl_sec: int,
    nonce: str = "",
    origin: str = "",
) -> Dict[str, Any]:
    now = int(time.time())
    claims = decode_jwt_claims(str(oauth_payload.get("access_token") or ""))
    return {
        "connected_integration_id": connected_integration_id,
        "oauth": oauth_payload,
        "user": public_claims(claims),
        "nonce": str(nonce or "").strip(),
        "origin": str(origin or "").strip(),
        "created_at": now,
        "expires_at": now + max(int(ttl_sec), 1),
    }


def access_token_from_session(session: Optional[Dict[str, Any]]) -> str:
    if not isinstance(session, dict):
        return ""
    oauth_payload = session.get("oauth") if isinstance(session.get("oauth"), dict) else {}
    return str(oauth_payload.get("access_token") or "").strip()
