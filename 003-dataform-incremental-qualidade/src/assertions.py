"""Executa localmente assertions equivalentes às de uma tabela Dataform."""
from __future__ import annotations
import argparse,csv,json
from collections import Counter
from decimal import Decimal
from pathlib import Path
def executar(entrada:Path,relatorio:Path)->dict:
 with entrada.open(newline="",encoding="utf-8") as f:rows=list(csv.DictReader(f))
 ids=Counter(r["order_id"] for r in rows);falhas={"uniqueKey":[k for k,v in ids.items() if v>1],"nonNull":[i+2 for i,r in enumerate(rows) if not all(r.values())],"rowConditions":[i+2 for i,r in enumerate(rows) if Decimal(r["amount"])<=0]};resultado={"status":"failed" if any(falhas.values()) else "passed","rows":len(rows),"failures":falhas};relatorio.parent.mkdir(parents=True,exist_ok=True);relatorio.write_text(json.dumps(resultado,indent=2)+"\n");return resultado
def main():
 p=argparse.ArgumentParser();p.add_argument("--input",type=Path,default=Path("data/orders.csv"));p.add_argument("--report",type=Path,default=Path("data/output/assertions.json"));a=p.parse_args();print(json.dumps(executar(a.input,a.report),indent=2))
if __name__=="__main__":main()
