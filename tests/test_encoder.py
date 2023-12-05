
# Check indexing is correct between reference and other stuff
# Can zip ref, alt, call
# Check that col sums are equal to 1
# Check that there are twwice as many 0.5s as there are artifical SNPs

import unittest
from src.encoder import Encoder

class TestConstructor(unittest.TestCase):
    def test_constructor_from_list(self):
        z = Encoder("A", {0: ["A", ".", "0/0"]})
    def test_constructor_from_tuple(self):
        z = Encoder("A", {0: ("A", ".", "0/0")})
        
if __name__ == '__main__':
    unittest.main()