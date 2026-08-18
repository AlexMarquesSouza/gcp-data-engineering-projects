import tempfile,unittest
from pathlib import Path
from src.advisor import executar
class T(unittest.TestCase):
 def test_order(self):
  r=Path(__file__).parents[1]
  with tempfile.TemporaryDirectory() as t:
   x=executar(r/"workload.json",Path(t)/"r.json");self.assertEqual(x["cluster_by"][:2],["customer_id","product_id"])
