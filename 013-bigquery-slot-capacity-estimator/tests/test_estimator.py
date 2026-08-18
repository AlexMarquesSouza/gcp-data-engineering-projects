import unittest
from src.estimator import estimate,percentile
class TestEstimator(unittest.TestCase):
    def test_percentile(self): self.assertEqual(percentile([10,20,30,40],.95),40)
    def test_capacity_with_headroom(self):
        rows=[{"slot_ms":"1000","duration_ms":"10"},{"slot_ms":"2000","duration_ms":"10"}]; r=estimate(rows,.2); self.assertEqual(r["p95_slots"],200); self.assertEqual(r["recommended_max_slots"],300)
    def test_empty(self): self.assertEqual(estimate([])["recommended_max_slots"],0)
if __name__=="__main__": unittest.main()
