import tempfile,unittest
from pathlib import Path
from src.late import executar
class T(unittest.TestCase):
 def test_late(self):
  r=Path(__file__).parents[1]
  with tempfile.TemporaryDirectory() as t:
   x=executar(r/"data/events.jsonl",Path(t)/"r.json");self.assertEqual((x["accepted"],x["late_dropped"]),(2,1));self.assertEqual(x["events"][2]["delay_minutes"],9)
