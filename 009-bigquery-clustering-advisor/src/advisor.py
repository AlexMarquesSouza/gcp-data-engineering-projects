import argparse,json
from pathlib import Path
def executar(inp,out):
 w=json.loads(inp.read_text());rank=sorted(w["filters"],key=lambda c:(w["filters"][c],w["cardinality"][c]),reverse=True)[:4];res={"cluster_by":rank,"ddl":"CLUSTER BY "+", ".join(rank),"note":"ordem prioriza filtros frequentes"};out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(res,indent=2)+"\n");return res
def main():
 p=argparse.ArgumentParser();p.add_argument("--input",type=Path,default=Path("workload.json"));p.add_argument("--output",type=Path,default=Path("data/output/advice.json"));a=p.parse_args();print(json.dumps(executar(a.input,a.output),indent=2))
if __name__=="__main__":main()
