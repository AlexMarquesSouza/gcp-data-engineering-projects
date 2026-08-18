import unittest
from src.metadata import validate
class TestMetadata(unittest.TestCase):
    def test_complete(self):
        r=validate([{"name":"a","aspects":{"owner":"team","domain":"sales"}}],["owner","domain"]); self.assertTrue(r["valid"]); self.assertEqual(r["average_score"],100)
    def test_missing(self):
        r=validate([{"name":"a","aspects":{"owner":"team"}}],["owner","domain"]); self.assertFalse(r["valid"]); self.assertEqual(r["entries"][0]["score"],50)
if __name__=="__main__": unittest.main()
