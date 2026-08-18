import argparse, csv, json
from pathlib import Path
def visible_rows(rows,principal,policies):
    applicable=[p for p in policies if principal in p["grantees"]]
    visible=[]
    for row in rows:
        if any(row.get(p["column"]) in p["allowed_values"] for p in applicable): visible.append(row)
    return visible
def audit(rows,principals,policies):
    results=[]
    for principal in principals:
        selected=visible_rows(rows,principal,policies); results.append({"principal":principal,"visible_rows":len(selected),"order_ids":[x["order_id"] for x in selected]})
    return {"total_rows":len(rows),"results":results}
def main():
    p=argparse.ArgumentParser(); p.add_argument("--rows",default="data/orders.csv"); p.add_argument("--policies",default="data/policies.json"); p.add_argument("--output",default="data/output/report.json"); a=p.parse_args()
    with open(a.rows,encoding="utf-8",newline="") as f: rows=list(csv.DictReader(f))
    doc=json.loads(Path(a.policies).read_text()); report=audit(rows,doc["principals_to_test"],doc["policies"]); out=Path(a.output); out.parent.mkdir(parents=True,exist_ok=True); out.write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n"); print(json.dumps(report,ensure_ascii=False,indent=2))
if __name__=="__main__": main()
