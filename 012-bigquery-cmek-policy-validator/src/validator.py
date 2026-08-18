import argparse,json,re
from pathlib import Path
KEY=re.compile(r"^projects/[^/]+/locations/([^/]+)/keyRings/[^/]+/cryptoKeys/[^/]+$")
def compatible(dataset_location,key_location):
    return dataset_location.lower()==key_location.lower()
def validate(assets):
    findings=[]
    for asset in assets:
        key=asset.get("kms_key_name",""); match=KEY.match(key)
        if not key: findings.append({"asset":asset["name"],"severity":"HIGH","reason":"CMEK ausente"})
        elif not match: findings.append({"asset":asset["name"],"severity":"HIGH","reason":"resource name da chave inválido"})
        elif not compatible(asset["location"],match.group(1)): findings.append({"asset":asset["name"],"severity":"HIGH","reason":f'localidade incompatível: dataset={asset["location"]}, key={match.group(1)}'})
    return {"compliant":not findings,"assets_checked":len(assets),"findings":findings}
def main():
    p=argparse.ArgumentParser(); p.add_argument("input",nargs="?",default="data/assets.json"); p.add_argument("--output",default="data/output/report.json"); a=p.parse_args(); report=validate(json.loads(Path(a.input).read_text())["assets"]); out=Path(a.output); out.parent.mkdir(parents=True,exist_ok=True); out.write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n"); print(json.dumps(report,ensure_ascii=False,indent=2)); raise SystemExit(0 if report["compliant"] else 2)
if __name__=="__main__": main()
