"""Valida pedidos e prepara arquivos e comando de carga do BigQuery."""
from __future__ import annotations
import argparse,csv,json
from datetime import date
from decimal import Decimal,InvalidOperation
from pathlib import Path

def executar(entrada:Path,saida:Path,projeto="SEU_PROJETO",dataset="dados")->dict:
    grupos={};rejeitados=[]
    with entrada.open(newline="",encoding="utf-8") as f:
        leitor=csv.DictReader(f)
        if leitor.fieldnames != ["pedido_id","data_pedido","cliente_id","valor"]: raise ValueError("schema inesperado")
        for n,linha in enumerate(leitor,start=2):
            try: dia=date.fromisoformat(linha["data_pedido"]); valor=Decimal(linha["valor"])
            except (ValueError,InvalidOperation): rejeitados.append({"linha":n,"motivo":"tipo invalido"});continue
            if valor<=0: rejeitados.append({"linha":n,"motivo":"valor deve ser positivo"});continue
            grupos.setdefault(dia.isoformat(),[]).append(linha)
    saida.mkdir(parents=True,exist_ok=True);arquivos=[]
    for dia,linhas in sorted(grupos.items()):
        alvo=saida/f"pedidos_{dia}.csv"
        with alvo.open("w",newline="",encoding="utf-8") as f:w=csv.DictWriter(f,fieldnames=["pedido_id","data_pedido","cliente_id","valor"]);w.writeheader();w.writerows(linhas)
        arquivos.append(str(alvo))
    schema=[{"name":"pedido_id","type":"STRING","mode":"REQUIRED"},{"name":"data_pedido","type":"DATE","mode":"REQUIRED"},{"name":"cliente_id","type":"STRING","mode":"REQUIRED"},{"name":"valor","type":"NUMERIC","mode":"REQUIRED"}]
    (saida/"schema.json").write_text(json.dumps(schema,indent=2)+"\n",encoding="utf-8")
    comando=f"bq load --source_format=CSV --skip_leading_rows=1 --time_partitioning_field=data_pedido {projeto}:{dataset}.pedidos 'gs://SEU_BUCKET/pedidos_*.csv' {saida}/schema.json"
    (saida/"comando_bq.txt").write_text(comando+"\n",encoding="utf-8")
    return {"particoes":len(grupos),"registros_validos":sum(map(len,grupos.values())),"rejeitados":rejeitados,"arquivos":arquivos}
def main():
    p=argparse.ArgumentParser();p.add_argument("--input",type=Path,default=Path("data/input/pedidos.csv"));p.add_argument("--output",type=Path,default=Path("data/output"));a=p.parse_args();print(json.dumps(executar(a.input,a.output),indent=2))
if __name__=="__main__":main()
