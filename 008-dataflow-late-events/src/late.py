import argparse,json
from datetime import datetime,timedelta
from pathlib import Path
def dt(x):return datetime.fromisoformat(x.replace("Z","+00:00"))
def executar(inp,out,allowed=5):
 rows=[]
 for line in inp.read_text().splitlines():
  e=json.loads(line);delay=(dt(e["arrival_time"])-dt(e["event_time"])).total_seconds()/60;e["delay_minutes"]=delay;e["classification"]="accepted" if delay<=allowed else "late_dropped";rows.append(e)
 res={"allowed_lateness_minutes":allowed,"accepted":sum(x["classification"]=="accepted" for x in rows),"late_dropped":sum(x["classification"]=="late_dropped" for x in rows),"events":rows};out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(res,indent=2)+"\n");return res
def main():
 p=argparse.ArgumentParser();p.add_argument("--input",type=Path,default=Path("data/events.jsonl"));p.add_argument("--output",type=Path,default=Path("data/output/report.json"));a=p.parse_args();print(json.dumps(executar(a.input,a.output),indent=2))
if __name__=="__main__":main()
