import tempfile,unittest
from pathlib import Path
from src.assertions import executar
class TestAssertions(unittest.TestCase):
 def test_detecta_duplicidade_e_valor_invalido(self):
  raiz=Path(__file__).parents[1]
  with tempfile.TemporaryDirectory() as t:
   r=executar(raiz/"data/orders.csv",Path(t)/"r.json");self.assertEqual(r["status"],"failed");self.assertEqual(r["failures"]["uniqueKey"],["o-2"]);self.assertEqual(r["failures"]["rowConditions"],[5])
if __name__=="__main__":unittest.main()
