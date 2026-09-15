from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="Uganda National Grid — Register of Systems")

SYSTEMS = [
("Legislative","Parliament of Uganda","parliament"),
("Cabinet","UNG-CABINET","cabinet"),("Cabinet","Office of the President","president"),("Cabinet","State House","statehouse"),("Cabinet","Office of the Prime Minister","opm"),
("Executive","Ministry of Defence","defence"),("Executive","Ministry of Foreign Affairs","diplomat"),("Executive","Ministry of Internal Affairs","internal"),("Executive","Ministry of Finance, Planning and Economic Development","treasury"),("Executive","Ministry of Justice and Constitutional Affairs","justice"),("Executive","Ministry of Public Service","service"),("Executive","Ministry of Energy and Minerals","energy"),("Executive","Ministry of East African Affairs","eac"),("Executive","Ministry of Health","vital"),("Executive","Ministry of Education and Sports","educate"),("Executive","Ministry of Agriculture, Animal Industry and Fisheries","harvest"),("Executive","Ministry of Local Government","localgov"),("Executive","Ministry of Lands, Housing & Urban Development","lands"),("Executive","Ministry of Trade, Industry and Co-operatives","trade"),("Executive","Ministry of Works and Transport","works"),("Executive","Ministry of Gender, Labour and Social Development","social"),("Executive","Ministry of Water and Environment","water"),("Executive","Ministry of Information and Communications Technology","ict"),("Executive","Ministry of Tourism, Wildlife and Antiquities","tourism"),("Executive","Kampala Capital City Authority","kcca")]

@app.get('/health')
def health(): return {'status':'ok','systems':len(SYSTEMS)}

@app.get('/api/systems')
def systems(): return [{'branch':b,'name':n,'slug':s} for b,n,s in SYSTEMS]

@app.get('/', response_class=HTMLResponse)
def index():
    cards=''.join(f'<a class="card {b.lower()}" href="/{s}"><small>{b}</small><strong>{n}</strong><span>Open system →</span></a>' for b,n,s in SYSTEMS)
    return f'''<!doctype html><html><head><meta name="viewport" content="width=device-width,initial-scale=1"><title>Uganda National Grid — Register of Systems</title><style>:root{{--ink:#141311;--paper:#f7f3e8;--panel:#fffdf7;--line:#ddd4bd;--forest:#2f5535;--gold:#a3821a;--cobalt:#2d4f8f}}*{{box-sizing:border-box}}body{{margin:0;background:var(--paper);color:var(--ink);font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif}}header{{padding:42px max(24px,6vw);border-bottom:1px solid var(--line)}}h1{{font-family:Georgia,serif;font-size:clamp(32px,5vw,60px);margin:0 0 10px}}header p{{max-width:760px;color:#6b6455}}main{{padding:32px max(24px,6vw);display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:14px}}.card{{background:var(--panel);border:1px solid var(--line);border-top:5px solid var(--cobalt);padding:22px;min-height:145px;text-decoration:none;color:inherit;display:flex;flex-direction:column;gap:10px;border-radius:8px}}.card.legislative{{border-top-color:var(--forest)}}.card.cabinet{{border-top-color:var(--gold)}}small{{text-transform:uppercase;letter-spacing:.12em}}strong{{font-family:Georgia,serif;font-size:20px}}span{{margin-top:auto;color:#6b6455}}footer{{padding:24px max(24px,6vw);border-top:1px solid var(--line);color:#6b6455}}</style></head><body><header><h1>Uganda National Grid</h1><p>Register of Systems · 25 independent government workspaces organized across the Legislative, Cabinet and Executive branches.</p></header><main>{cards}</main><footer>UNG Government Systems Register · 25 systems</footer></body></html>'''

@app.get('/{slug}', response_class=HTMLResponse)
def system_page(slug:str):
    row=next((x for x in SYSTEMS if x[2]==slug),None)
    if not row: return HTMLResponse('<h1>System not found</h1>',status_code=404)
    b,n,s=row
    return f'''<!doctype html><html><head><meta name="viewport" content="width=device-width,initial-scale=1"><title>{n}</title><style>body{{margin:0;background:#f7f3e8;color:#141311;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif}}main{{max-width:900px;margin:auto;padding:8vw 28px}}a{{color:#2d4f8f}}h1{{font:48px Georgia,serif}}.panel{{background:#fffdf7;border:1px solid #ddd4bd;border-radius:10px;padding:28px;margin-top:28px}}</style></head><body><main><a href="/">← Government Register</a><p>{b}</p><h1>{n}</h1><div class="panel"><h2>System workspace</h2><p>This route is registered and ready for the {n} application to be connected.</p><p><b>System slug:</b> {s}</p></div></main></body></html>'''
