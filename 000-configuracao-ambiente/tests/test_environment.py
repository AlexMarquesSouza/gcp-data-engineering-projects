import unittest
from src.check_environment import inspect_environment
class TestEnvironment(unittest.TestCase):
    def test_report_contract(self):
        r=inspect_environment(); self.assertIn("python",r); self.assertIn("gcloud",r["tools"]); self.assertIn("bq",r["tools"])
if __name__=="__main__": unittest.main()
