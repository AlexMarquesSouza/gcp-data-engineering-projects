import argparse,csv,json,math
from pathlib import Path
def percentile(values,p):
    if not values:return 0
    ordered=sorted(values); return ordered[math.ceil(len(ordered)*p)-1]
def estimate(rows,headroom=0.2):
    slots=[float(x["slot_ms"])/float(x["duration_ms"]) for x in rows if float(x["duration_ms"])>0]
    p95=percentile(slots,.95); recommended=math.ceil(p95*(1+headroom)/100)*100 if p95 else 0
    return {"jobs_analyzed":len(slots),"average_slots":round(sum(slots)/len(slots),1) if slots else 0,"p95_slots":round(p95,1),"headroom_percent":round(headroom*100),"recommended_max_slots":recommended}
def main():
    p=argparse.ArgumentParser(); p.add_argument("input",nargs="?",default="data/jobs.csv"); p.add_argument("--output",default="data/output/report.json"); a=p.parse_args()
    with open(a.input,encoding="utf-8",newline="") as f: rows=list(csv.DictReader(f))
    report=estimate(rows); out=Path(a.output); out.parent.mkdir(parents=True,exist_ok=True); out.write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n"); print(json.dumps(report,ensure_ascii=False,indent=2))
if __name__=="__main__": main()
