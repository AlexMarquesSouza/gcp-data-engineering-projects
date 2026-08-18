"""Valida e executa um DAG local respeitando dependências e retries."""
from __future__ import annotations
import argparse,json
from pathlib import Path
def executar(definicao:Path,saida:Path)->dict:
 cfg=json.loads(definicao.read_text());tasks=cfg["tasks"];pendentes=set(tasks);sucesso=set();historico=[]
 while pendentes:
  prontos=sorted(t for t in pendentes if set(tasks[t]["upstream"])<=sucesso)
  if not prontos:raise ValueError("DAG possui ciclo ou dependência ausente")
  for task in prontos:
   max_attempts=cfg["retries"]+1;falhas=tasks[task]["failures_before_success"]
   for attempt in range(1,max_attempts+1):
    status="failed" if attempt<=falhas else "success";historico.append({"task":task,"attempt":attempt,"status":status})
    if status=="success":sucesso.add(task);pendentes.remove(task);break
   else:return {"status":"failed","history":historico}
 resultado={"status":"success","order":[x["task"] for x in historico if x["status"]=="success"],"history":historico};saida.parent.mkdir(parents=True,exist_ok=True);saida.write_text(json.dumps(resultado,indent=2)+"\n");return resultado
def main():
 p=argparse.ArgumentParser();p.add_argument("--dag",type=Path,default=Path("dag.json"));p.add_argument("--output",type=Path,default=Path("data/output/dag-run.json"));a=p.parse_args();print(json.dumps(executar(a.dag,a.output),indent=2))
if __name__=="__main__":main()
