import argparse, json
from pathlib import Path
def validate(entries,required):
    results=[]
    for entry in entries:
        missing=[x for x in required if not entry.get("aspects",{}).get(x)]; score=round(100*(len(required)-len(missing))/len(required)) if required else 100; results.append({"entry":entry["name"],"score":score,"missing_aspects":missing})
    average=round(sum(x["score"] for x in results)/len(results)) if results else 100
    return {"valid":all(not x["missing_aspects"] for x in results),"average_score":average,"entries":results}
def main():
    p=argparse.ArgumentParser(); p.add_argument("input",nargs="?",default="data/entries.json"); p.add_argument("--output",default="data/output/report.json"); a=p.parse_args(); doc=json.loads(Path(a.input).read_text(encoding="utf-8")); report=validate(doc["entries"],doc["required_aspects"]); out=Path(a.output); out.parent.mkdir(parents=True,exist_ok=True); out.write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n",encoding="utf-8"); print(json.dumps(report,ensure_ascii=False,indent=2)); raise SystemExit(0 if report["valid"] else 2)
if __name__=="__main__": main()
