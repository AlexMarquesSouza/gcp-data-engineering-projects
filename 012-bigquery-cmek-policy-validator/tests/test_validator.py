import unittest
from src.validator import validate
class TestValidator(unittest.TestCase):
    def test_matching_location(self):
        a=[{"name":"d","location":"us-central1","kms_key_name":"projects/p/locations/us-central1/keyRings/r/cryptoKeys/k"}]; self.assertTrue(validate(a)["compliant"])
    def test_missing_key(self): self.assertFalse(validate([{"name":"d","location":"US"}])["compliant"])
    def test_wrong_location(self):
        a=[{"name":"d","location":"EU","kms_key_name":"projects/p/locations/US/keyRings/r/cryptoKeys/k"}]; self.assertIn("incompatível",validate(a)["findings"][0]["reason"])
if __name__=="__main__": unittest.main()
