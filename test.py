import unittest
from mask import cidrConvertion

TEST_CASES = (
    ('255.255.255.0', 24),
    ('255.255.255.255', 32)
)

OUT_BOUWNDRY_CASE = ('255.255.256.0', -1)

class CidrToMaskTestCase(unittest.TestCase):
    
    def test_valid_cidr_to_mask(self):
        for test_case in TEST_CASES:
            cidr, mask = test_case
            with self.subTest(cidr):
                self.assertEqual(mask, cidrConvertion(cidr))


    def test_valid_cidr_boundary(self):
        cidr, mask = OUT_BOUWNDRY_CASE
        self.assertEqual(mask, cidrConvertion(cidr))
if __name__ == '__main__': 
    unittest.main()
