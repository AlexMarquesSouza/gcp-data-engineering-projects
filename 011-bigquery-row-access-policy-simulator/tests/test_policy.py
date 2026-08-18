import unittest
from src.policy import visible_rows
class TestPolicy(unittest.TestCase):
    def setUp(self): self.rows=[{"order_id":"1","region":"S"},{"order_id":"2","region":"N"}]; self.p=[{"grantees":["group:s"],"column":"region","allowed_values":["S"]},{"grantees":["group:all"],"column":"region","allowed_values":["S","N"]}]
    def test_regional(self): self.assertEqual(len(visible_rows(self.rows,"group:s",self.p)),1)
    def test_union_and_unknown(self): self.assertEqual(len(visible_rows(self.rows,"group:all",self.p)),2); self.assertEqual(visible_rows(self.rows,"unknown",self.p),[])
if __name__=="__main__": unittest.main()
