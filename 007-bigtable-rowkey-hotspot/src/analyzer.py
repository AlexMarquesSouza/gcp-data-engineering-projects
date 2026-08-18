"""Detecta prefixos sequenciais e propõe buckets determinísticos."""
from __future__ import annotations
import argparse,csv,hashlib,json
from collections import Counter
from pathlib import Path
def executar(entrada:Path,saida:Path,buckets:int=8)->dict:
 with entrada.open(newline="",encoding="utf-8") as f:rows=list(csv.DictReader(f))
 prefixos=Counter(r["row_key"].split("#")[0] for r in rows);maior=max(prefixos.values())/len(rows);sugestoes=[]
 for r in rows:
  partes=r["row_key"].split("#");sensor=partes[1];bucket=int(hashlib.sha256(sensor.encode()).hexdigest(),16)%buckets;sugestoes.append({"original":r["row_key"],"suggested":f"{bucket:02d}#{sensor}#{partes[0]}#{partes[2]}"})
 resultado={"sequential_prefix_share_pct":round(maior*100,2),"hotspot_risk":"high" if maior>.5 else "acceptable","bucket_count":buckets,"examples":sugestoes};saida.parent.mkdir(parents=True,exist_ok=True);saida.write_text(json.dumps(resultado,indent=2)+"\n");return resultado
def main():
 p=argparse.ArgumentParser();p.add_argument("--input",type=Path,default=Path("data/writes.csv"));p.add_argument("--output",type=Path,default=Path("data/output/rowkey-report.json"));a=p.parse_args();print(json.dumps(executar(a.input,a.output),indent=2))
if __name__=="__main__":main()
