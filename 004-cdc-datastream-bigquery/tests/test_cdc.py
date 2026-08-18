import tempfile,unittest
from pathlib import Path
from src.cdc_merge import executar
class TestCDC(unittest.TestCase):
 def test_aplica_insert_update_delete_e_deduplica(self):
  raiz=Path(__file__).parents[1]
  with tempfile.TemporaryDirectory() as t:
   r=executar(raiz/"data/initial.json",raiz/"data/changes.jsonl",Path(t)/"r.json");self.assertEqual(r["events_applied"],3);self.assertEqual(r["duplicates_ignored"],1);self.assertEqual([x["customer_id"] for x in r["rows"]],["c1","c3"]);self.assertEqual(r["rows"][0]["city"],"Campinas")
if __name__=="__main__":unittest.main()
