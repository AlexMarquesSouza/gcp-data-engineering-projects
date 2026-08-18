import tempfile,unittest
from pathlib import Path
from src.analyzer import executar
class TestAnalyzer(unittest.TestCase):
 def test_detecta_prefixo_temporal_e_antecipa_bucket(self):
  raiz=Path(__file__).parents[1]
  with tempfile.TemporaryDirectory() as t:
   r=executar(raiz/"data/writes.csv",Path(t)/"r.json");self.assertEqual(r["hotspot_risk"],"high");self.assertEqual(r["sequential_prefix_share_pct"],100.0);self.assertNotEqual(r["examples"][0]["original"].split("#")[0],r["examples"][0]["suggested"].split("#")[0])
if __name__=="__main__":unittest.main()
