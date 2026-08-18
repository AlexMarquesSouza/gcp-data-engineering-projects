import tempfile,unittest,json
from pathlib import Path
from src.dag_runner import executar
class TestDAG(unittest.TestCase):
 def test_dependencias_e_retry(self):
  raiz=Path(__file__).parents[1]
  with tempfile.TemporaryDirectory() as t:
   r=executar(raiz/"dag.json",Path(t)/"r.json");self.assertEqual(r["status"],"success");self.assertEqual(r["order"],["extract","validate","transform","load"]);self.assertEqual(len([x for x in r["history"] if x["task"]=="validate"]),2)
 def test_rejeita_ciclo(self):
  with tempfile.TemporaryDirectory() as t:
   p=Path(t);(p/"d.json").write_text(json.dumps({"tasks":{"a":{"upstream":["b"],"failures_before_success":0},"b":{"upstream":["a"],"failures_before_success":0}},"retries":0}));
   with self.assertRaises(ValueError):executar(p/"d.json",p/"r.json")
if __name__=="__main__":unittest.main()
