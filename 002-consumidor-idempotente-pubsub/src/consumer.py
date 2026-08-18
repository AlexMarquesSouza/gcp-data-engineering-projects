"""Simula consumidor Pub/Sub idempotente com dead-letter local."""
from __future__ import annotations
import argparse,json
from pathlib import Path
def executar(entrada:Path,saida:Path,estado:Path)->dict:
 processados=set(json.loads(estado.read_text())["message_ids"]) if estado.exists() else set();aceitos=[];dlq=[];duplicados=0
 for n,texto in enumerate(entrada.read_text(encoding="utf-8").splitlines(),start=1):
  if not texto.strip():continue
  try:msg=json.loads(texto);mid=msg["message_id"];valor=float(msg["payload"]["amount"])
  except (json.JSONDecodeError,KeyError,TypeError,ValueError):dlq.append({"linha":n,"motivo":"mensagem invalida","original":texto});continue
  if mid in processados:duplicados+=1;continue
  if valor<=0:dlq.append({"linha":n,"message_id":mid,"motivo":"amount deve ser positivo","original":msg});continue
  aceitos.append(msg);processados.add(mid)
 saida.mkdir(parents=True,exist_ok=True);(saida/"processed.jsonl").write_text("".join(json.dumps(x)+"\n" for x in aceitos),encoding="utf-8");(saida/"dead-letter.jsonl").write_text("".join(json.dumps(x)+"\n" for x in dlq),encoding="utf-8");estado.parent.mkdir(parents=True,exist_ok=True);estado.write_text(json.dumps({"message_ids":sorted(processados)},indent=2)+"\n")
 return {"processados":len(aceitos),"duplicados_ignorados":duplicados,"dead_letter":len(dlq)}
def main():
 p=argparse.ArgumentParser();p.add_argument("--input",type=Path,default=Path("data/messages.jsonl"));p.add_argument("--output",type=Path,default=Path("data/output"));p.add_argument("--state",type=Path,default=Path("state/processed.json"));a=p.parse_args();print(json.dumps(executar(a.input,a.output,a.state),indent=2))
if __name__=="__main__":main()
