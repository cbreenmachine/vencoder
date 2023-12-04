import unittest
from variant import VariantEncoder
from testdata import *

letters = [".", "A", "C", "G", "T"]
variants = ["0/0", "0/1", "1/1", "1/2"]


class TestOneHotEncoder(unittest.TestCase):

    def setUp(self):
        self.four_letters = VariantEncoder(
            four_letters_ref, four_letters_methy,
            four_letters_snp, 1
        )
        self.four_letters.encode_data()

        self.variant_calls = VariantEncoder(
            variant_calls_ref, variant_calls_methy,
            variant_calls_snp, 1
        )
        self.variant_calls.encode_data()

        self.fake_letter = VariantEncoder(
            other_chars_ref, other_chars_methy, 
            other_chars_snp, 1
        )
        self.fake_letter.encode_data()
        
    
    def test_vanilla(self):
        self.assertListEqual(self.four_letters.encoded_tensor, identity(4))

    def test_variants(self):
        self.assertListEqual(self.variant_calls.encoded_tensor, 
                            [[1,0,0,0], [0.5,0.5,0,0], 
                              [0,1,0,0], [0,0.5,0.25,0.25]])

    def test_fake_letter(self):
        self.assertListEqual(self.fake_letter.encoded_tensor, [[0, 0, 0, 0] for x in range(3)])
        

class TestHeterozygous(unittest.TestCase):
    def setUp(self):
        

if __name__ == '__main__':
    unittest.main()