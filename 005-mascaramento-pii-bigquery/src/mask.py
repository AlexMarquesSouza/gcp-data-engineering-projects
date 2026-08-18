"""Produz visão mascarada de PII sem expor valores no relatório."""
from __future__ import annotations
import argparse,csv,hashlib,json
from pathlib import Path
def digest(valor:str)->str:return hashlib.sha256(valor.encode()).hexdigest()
def executar(entrada:Path,saida:Path,perfil:str)->dict:
 with entrada.open(newline="",encoding="utf-8") as f:rows=list(csv.DictReader(f))
 out=[]
 for r in rows:
  if perfil=="privileged":out.append(r);continue
  out.append({**r,"email":digest(r["email"]),"tax_id":"***-***-**"+r["tax_id"][-2:]})
 saida.parent.mkdir(parents=True,exist_ok=True)
 with saida.open("w",newline="",encoding="utf-8") as f:w=csv.DictWriter(f,fieldnames=["customer_id","name","email","tax_id","city"]);w.writeheader();w.writerows(out)
 return {"profile":perfil,"rows":len(out),"masked_columns":[] if perfil=="privileged" else ["email","tax_id"]}
def main():
 p=argparse.ArgumentParser();p.add_argument("--input",type=Path,default=Path("data/customers.csv"));p.add_argument("--output",type=Path,default=Path("data/output/customers_masked.csv"));p.add_argument("--profile",choices=["analyst","privileged"],default="analyst");a=p.parse_args();print(json.dumps(executar(a.input,a.output,a.profile),indent=2))
if __name__=="__main__":main()
