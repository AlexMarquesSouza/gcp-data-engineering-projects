# Radar de Engenharia de Dados · GCP

| # | Projeto | Conceitos | Status |
|---:|---|---|---|
| 000 | [Configuração do ambiente](000-configuracao-ambiente/README.md) | VS Code, Python, Git, Google Cloud CLI opcional | Rascunho para revisão |
| 001 | [Carga particionada no BigQuery](001-carga-particionada-bigquery/README.md) | BigQuery, schema, partições | Rascunho para revisão |
| 002 | [Consumidor idempotente Pub/Sub](002-consumidor-idempotente-pubsub/README.md) | Pub/Sub, deduplicação, dead-letter | Rascunho para revisão |
| 003 | [Dataform incremental com qualidade](003-dataform-incremental-qualidade/README.md) | Dataform, BigQuery, assertions | Rascunho para revisão |
| 004 | [CDC com Datastream e BigQuery](004-cdc-datastream-bigquery/README.md) | Datastream, CDC, merge | Rascunho para revisão |
| 005 | [Mascaramento de PII no BigQuery](005-mascaramento-pii-bigquery/README.md) | Segurança em coluna, tags, data policies | Rascunho para revisão |
| 006 | [DAG com dependências no Composer](006-composer-dag-dependencies/README.md) | Airflow, DAG, retries | Rascunho para revisão |
| 007 | [Detector de hotspots Bigtable](007-bigtable-rowkey-hotspot/README.md) | Bigtable, row key, bucketing | Rascunho para revisão |
| 008 | [Eventos atrasados no Dataflow](008-dataflow-late-events/README.md) | Dataflow, watermark, late data | Rascunho para revisão |
| 009 | [Advisor de clustering BigQuery](009-bigquery-clustering-advisor/README.md) | BigQuery, clustering, pruning | Rascunho para revisão |
| 010 | [Validador de metadados do catálogo](010-knowledge-catalog-metadata-validator/README.md) | Dataplex, aspectos, completude | Rascunho para revisão |
| 011 | [Simulador de Row Access Policies](011-bigquery-row-access-policy-simulator/README.md) | BigQuery, row-level security, IAM | Rascunho para revisão |
| 012 | [Validador de política CMEK](012-bigquery-cmek-policy-validator/README.md) | BigQuery, Cloud KMS, criptografia | Rascunho para revisão |
| 013 | [Estimador de capacidade em slots](013-bigquery-slot-capacity-estimator/README.md) | BigQuery, slots, P95, capacidade | Rascunho para revisão |

Nenhum projeto pode ser publicado ou implantado sem aprovação manual.


## Manutenção deste repositório

Este diretório é autônomo: contém documentação, dependências do site, testes estruturais e scripts próprios. Após clonar:

```bash
cd "caminho/para/gcp-data-engineering-projects"
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements-docs.txt
python3 scripts/validate_projects.py
bash scripts/build_site.sh
```

O build gera somente documentação local. Publicação, criação de repositório remoto e `git push` continuam manuais.
