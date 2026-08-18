import tempfile,unittest
from pathlib import Path
from src.consumer import executar
class TestConsumer(unittest.TestCase):
 def test_deduplica_e_separa_dead_letter(self):
  raiz=Path(__file__).parents[1]
  with tempfile.TemporaryDirectory() as t:
   p=Path(t);r=executar(raiz/"data/messages.jsonl",p/"out",p/"state.json");self.assertEqual(r,{"processados":2,"duplicados_ignorados":1,"dead_letter":1})
 def test_ignora_linhas_vazias(self):
  with tempfile.TemporaryDirectory() as t:
   p=Path(t);entrada=p/"m.jsonl";entrada.write_text("\n\n",encoding="utf-8");r=executar(entrada,p/"out",p/"state.json");self.assertEqual(r,{"processados":0,"duplicados_ignorados":0,"dead_letter":0})
 def test_reexecucao_nao_reprocessa_sucessos(self):
  raiz=Path(__file__).parents[1]
  with tempfile.TemporaryDirectory() as t:
   p=Path(t);executar(raiz/"data/messages.jsonl",p/"out",p/"state.json");r=executar(raiz/"data/messages.jsonl",p/"out",p/"state.json");self.assertEqual(r["processados"],0)
if __name__=="__main__":unittest.main()
