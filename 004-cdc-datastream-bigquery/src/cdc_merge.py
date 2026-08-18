"""Aplica eventos CDC ordenados e deduplicados no modo merge."""
from __future__ import annotations
import argparse,json
from pathlib import Path
def executar(inicial:Path,mudancas:Path,saida:Path)->dict:
 tabela={r["customer_id"]:r for r in json.loads(inicial.read_text())};eventos=[json.loads(x) for x in mudancas.read_text().splitlines() if x.strip()];vistos=set();aplicados=duplicados=0
 for e in sorted(eventos,key=lambda x:x["sequence"]):
  if e["uuid"] in vistos:duplicados+=1;continue
  vistos.add(e["uuid"]);chave=e["row"]["customer_id"]
  if e["change_type"]=="DELETE":tabela.pop(chave,None)
  elif e["change_type"] in {"INSERT","UPDATE-INSERT"}:tabela[chave]=e["row"]
  else:raise ValueError("change_type desconhecido")
  aplicados+=1
 resultado={"rows":sorted(tabela.values(),key=lambda x:x["customer_id"]),"events_applied":aplicados,"duplicates_ignored":duplicados};saida.parent.mkdir(parents=True,exist_ok=True);saida.write_text(json.dumps(resultado,indent=2,ensure_ascii=False)+"\n");return resultado
def main():
 p=argparse.ArgumentParser();p.add_argument("--initial",type=Path,default=Path("data/initial.json"));p.add_argument("--changes",type=Path,default=Path("data/changes.jsonl"));p.add_argument("--output",type=Path,default=Path("data/output/customers.json"));a=p.parse_args();print(json.dumps(executar(a.initial,a.changes,a.output),indent=2,ensure_ascii=False))
if __name__=="__main__":main()
