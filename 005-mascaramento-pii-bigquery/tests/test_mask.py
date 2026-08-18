import csv,tempfile,unittest
from pathlib import Path
from src.mask import executar
class TestMask(unittest.TestCase):
 def test_analista_nao_recebe_pii_bruta(self):
  raiz=Path(__file__).parents[1]
  with tempfile.TemporaryDirectory() as t:
   out=Path(t)/"x.csv";r=executar(raiz/"data/customers.csv",out,"analyst")
   with out.open(newline="",encoding="utf-8") as arquivo:rows=list(csv.DictReader(arquivo))
   self.assertEqual(r["masked_columns"],["email","tax_id"]);self.assertNotIn("@",rows[0]["email"]);self.assertEqual(rows[0]["tax_id"],"***-***-**01")
if __name__=="__main__":unittest.main()
