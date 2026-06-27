import fs from 'fs';
const R='C:/Users/uvays/Projects/py-integrations/.understand-anything/intermediate/';
const T='C:/Users/uvays/Projects/py-integrations/.understand-anything/tmp/';
const ext=JSON.parse(fs.readFileSync(T+'ua-file-extract-results-1.json','utf8'));
const batches=JSON.parse(fs.readFileSync(R+'batches.json','utf8'));
const x=batches.batches.find(z=>z.batchIndex===1);
const bd=x.batchImportData||{};

const nodes=[]; const edges=[];
const nameOf=p=>p.split('/').pop();

// per-file metadata: summary + tags
const meta={
 'clients/asterisk_crm_channel/main.py':['Asterisk PBX CRM channel integration that ingests AMI call events, normalizes phone numbers and call direction, resolves leads, and writes call records into REGOS CRM tickets.',['crm-channel','telephony','integration','service','data-pipeline']],
 'clients/base.py':['Abstract base class for all integration clients defining the common lifecycle and request-handling contract.',['integration','base-class','abstract','contract']],
 'clients/billing_connector/main.py':['Billing connector integration that normalizes billing webhook payloads, renders templated CRM messages, and syncs billing client/ticket snapshots into REGOS.',['integration','billing','webhook','crm','service']],
 'clients/bitrix24/main.py':['Thin Bitrix24 TSD integration client exposing a small set of CRM actions over the REGOS API.',['integration','crm','bitrix24','service']],
 'clients/edo_didox/main.py':['Didox EDO (electronic document) integration providing a Didox API client and document/invoice/contract syncing into REGOS.',['integration','edo','e-invoicing','service','api-handler']],
 'clients/edo_fakturauz/main.py':['Faktura.uz EDO integration providing a Faktura.uz API client and electronic invoice/contract document syncing into REGOS.',['integration','edo','e-invoicing','service','api-handler']],
 'clients/email_sender/main.py':['Email sender integration that dispatches transactional emails via configured SMTP/email provider settings.',['integration','email','notification','service']],
 'clients/eskiz_sms/main.py':['Eskiz SMS gateway integration for sending SMS messages and managing the provider auth token.',['integration','sms','gateway','service']],
 'clients/getsms/main.py':['GetSMS gateway integration for sending SMS messages through the GetSMS provider API.',['integration','sms','gateway','service']],
 'clients/marketplace_toserver/main.py':['ToServer marketplace integration that synchronizes item stock and pricing to the marketplace on a schedule.',['integration','marketplace','sync','scheduler','service']],
 'clients/marketplace_uzum_tezkor/main.py':['Uzum Tezkor marketplace integration handling menu/item sync, order delivery webhooks, and order status mapping.',['integration','marketplace','webhook','orders','service']],
 'clients/marketplace_yandex_eats/main.py':['Yandex Eats marketplace integration handling menu sync, order delivery events, and order status mapping with REGOS.',['integration','marketplace','webhook','orders','service']],
 'clients/regos_pay_deals/main.py':['REGOS Pay deals integration that normalizes payment webhooks, formats deal amounts, and links payments to CRM deals/pipelines.',['integration','payment','webhook','crm','service']],
 'clients/telegram_bot_quantity/handlers/get_quantity.py':['Telegram bot handler that fetches stock item quantities, filters them, and builds an Excel report for the requested stock.',['telegram','handler','reporting','excel','data-pipeline']],
 'clients/telegram_bot_quantity/main.py':['Telegram minimum-quantity bot integration that polls updates, tracks stock thresholds, and notifies chats about low item quantities.',['integration','telegram','bot','notification','service']],
 'clients/telegram_bot_quantity/services/send_messages.py':['Service helper that broadcasts a message to multiple Telegram chat IDs.',['telegram','service','messaging','utility']],
 'clients/telegram_bot_quantity/utils.py':['Utility helpers for the quantity bot: chat-id parsing, money/timestamp formatting, and chat-id extraction.',['telegram','utility','formatting','parsing']],
 'clients/telegram_polling.py':['Telegram long-polling manager that tracks active polling sessions per bot integration.',['telegram','polling','session-manager','infrastructure']],
 'clients/tsd/main.py':['TSD (terminal data collection) integration client exposing warehouse data-collection actions over REGOS.',['integration','tsd','warehouse','service']],
 'config/settings.py':['Central application settings loaded from environment, covering REGOS API, Redis, scheduler, and provider credentials.',['configuration','settings','environment','config']],
 'core/api/integrations/connected_integration.py':['Service wrapper for fetching and editing connected-integration records via the REGOS API.',['service','api-handler','integration','data-model']],
 'core/api/regos_api.py':['Core REGOS API client with retry handling and batch request support used by all integrations.',['api-handler','client','core','retry']],
 'core/redis.py':['Redis operations layer providing JSON caching, locks, TTL management, sets, sorted sets, and streams with a local fallback cache.',['core','redis','caching','infrastructure','utility']],
 'core/scheduler.py':['Client for the REGOS scheduler API to create and manage scheduled integration tasks.',['core','scheduler','api-handler','service']],
 'routes/clients.py':['FastAPI router dispatching integration, UI, and external webhook requests to the appropriate connected-integration client handlers.',['api-handler','router','entry-point','dispatcher','middleware']],
 'schemas/api/integrations/connected_integration.py':['Pydantic schemas for connected-integration records, including owner/handler enums, schedules, and get/edit request-response models.',['type-definition','schema-definition','data-model','pydantic']],
 'schemas/api/integrations/connected_integration_setting.py':['Pydantic schemas for connected-integration settings and their edit request payloads.',['type-definition','schema-definition','data-model','pydantic']],
 'schemas/integration/base.py':['Base Pydantic request/response and error models shared by all integration handlers.',['type-definition','schema-definition','data-model','pydantic']],
 'schemas/integration/email_integration_base.py':['Base integration schema specialization for email-sending integrations.',['type-definition','schema-definition','email','pydantic']],
 'schemas/integration/integration_base.py':['Base integration request model defining common fields for all integration requests.',['type-definition','schema-definition','data-model','pydantic']],
 'schemas/integration/sms_integration_base.py':['Base integration schema specialization for SMS-sending integrations.',['type-definition','schema-definition','sms','pydantic']],
 'schemas/scheduler.py':['Pydantic schemas for the REGOS scheduler API: schedules, tasks, period/status enums, and adapter request models.',['type-definition','schema-definition','scheduler','pydantic']],
};

const complexity=l=>l>200?'complex':l>=50?'moderate':'simple';

// significance filter
function sigFn(f){return (f.endLine-f.startLine+1)>=10;}
function sigCls(c){return (c.methods&&c.methods.length>=2)||(c.endLine-c.startLine+1)>=20;}

const exportedNames=r=>new Set((r.exports||[]).map(e=>e.name));

for(const r of ext.results){
  const p=r.path; const m=meta[p]||['Python module in the REGOS integrations service.',['integration','python','module']];
  nodes.push({id:'file:'+p,type:'file',name:nameOf(p),filePath:p,summary:m[0],tags:m[1],complexity:complexity(r.nonEmptyLines),languageNotes:undefined});
  const exp=exportedNames(r);
  // functions
  for(const f of (r.functions||[])){
    if(!(sigFn(f)||exp.has(f.name))) continue;
    const fid='function:'+p+':'+f.name;
    nodes.push({id:fid,type:'function',name:f.name,filePath:p,lineRange:[f.startLine,f.endLine],summary:'Helper function `'+f.name+'` in '+nameOf(p)+'.',tags:['utility','function','python'],complexity:complexity(f.endLine-f.startLine+1)});
    edges.push({source:'file:'+p,target:fid,type:'contains',direction:'forward',weight:1.0});
    if(exp.has(f.name)) edges.push({source:'file:'+p,target:fid,type:'exports',direction:'forward',weight:0.8});
  }
  // classes
  for(const c of (r.classes||[])){
    if(!(sigCls(c)||exp.has(c.name))) continue;
    const cid='class:'+p+':'+c.name;
    nodes.push({id:cid,type:'class',name:c.name,filePath:p,lineRange:[c.startLine,c.endLine],summary:'Class `'+c.name+'` defined in '+nameOf(p)+(c.methods&&c.methods.length?(' with '+c.methods.length+' methods.'):'.'),tags:['class','python',(c.methods&&c.methods.length>10)?'service':'data-model'],complexity:complexity(c.endLine-c.startLine+1)});
    edges.push({source:'file:'+p,target:cid,type:'contains',direction:'forward',weight:1.0});
    if(exp.has(c.name)) edges.push({source:'file:'+p,target:cid,type:'exports',direction:'forward',weight:0.8});
  }
}

// imports edges (1:1)
let impCount=0;
for(const p of Object.keys(bd)){
  for(const tgt of (bd[p]||[])){
    edges.push({source:'file:'+p,target:'file:'+tgt,type:'imports',direction:'forward',weight:0.7});
    impCount++;
  }
}

// clean undefined languageNotes
for(const n of nodes){ if(n.languageNotes===undefined) delete n.languageNotes; }

console.error('nodes',nodes.length,'edges',edges.length,'imports',impCount);

function filePathOfNode(n){ return n.filePath||null; }

// partition by file alphabetical, greedy bin-packing under caps (<=60 nodes, <=120 edges)
const files=ext.results.map(r=>r.path).sort();
// precompute per-file node count and source-edge count
const perFile={};
for(const f of files) perFile[f]={n:0,e:0};
for(const n of nodes){ const fp=filePathOfNode(n); if(fp&&perFile[fp]) perFile[fp].n++; }
const idsByFile={};
for(const n of nodes){ const fp=filePathOfNode(n); (idsByFile[fp]=idsByFile[fp]||new Set()).add(n.id); }
for(const f of files){ const ids=idsByFile[f]||new Set(); perFile[f].e=edges.filter(e=>ids.has(e.source)).length; }
const NCAP=60, ECAP=120;
const fileChunks=[]; let cur=new Set(), cn=0, ce=0;
for(const f of files){
  const fn=perFile[f].n, fe=perFile[f].e;
  if(cur.size>0 && (cn+fn>NCAP || ce+fe>ECAP)){ fileChunks.push(cur); cur=new Set(); cn=0; ce=0; }
  cur.add(f); cn+=fn; ce+=fe;
}
if(cur.size>0) fileChunks.push(cur);

const written=[];
fileChunks.forEach((set,idx)=>{
  const pn=nodes.filter(n=>set.has(filePathOfNode(n)));
  const ids=new Set(pn.map(n=>n.id));
  const pe=edges.filter(e=>ids.has(e.source));
  const out={nodes:pn,edges:pe};
  const fn=R+'batch-1-part-'+(idx+1)+'.json';
  fs.writeFileSync(fn,JSON.stringify(out,null,2));
  written.push([fn,pn.length,pe.length]);
});
console.error('parts',written.length);
written.forEach(w=>console.error(w[0],'n='+w[1],'e='+w[2]));
// sanity: all import edge sources should be covered
const allSrc=new Set(nodes.map(n=>n.id));
const missing=edges.filter(e=>!allSrc.has(e.source));
console.error('edges with missing source node:',missing.length);
