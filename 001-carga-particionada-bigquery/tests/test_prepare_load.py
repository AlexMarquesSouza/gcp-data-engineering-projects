import json,tempfile,unittest
from pathlib import Path
from src.prepare_load import executar
class TestCarga(unittest.TestCase):
 def test_prepara_particoes_schema_e_comando(self):
  raiz=Path(__file__).parents[1]
  with tempfile.TemporaryDirectory() as t:
   out=Path(t);r=executar(raiz/"data/input/pedidos.csv",out);self.assertEqual(r["particoes"],3);self.assertEqual(r["registros_validos"],4);self.assertEqual(json.loads((out/"schema.json").read_text())[1]["type"],"DATE");self.assertIn("--time_partitioning_field=data_pedido",(out/"comando_bq.txt").read_text())
if __name__=="__main__":unittest.main()
