import unittest
from base import OneHotEncoder
from testdata import *


def identity(n):
    '''Matrix in list of lists form that had ones on diagonal, zeros elsewhere'''
    return [[1 if i==j else 0 for j in range(n)] for i in range(n)]

class TestOneHotEncoder(unittest.TestCase):

    def setUp(self):
        self.four_letters = OneHotEncoder(
            four_letters_ref, four_letters_methy,
            four_letters_snp, 1
        )
        self.four_letters.encode_data()

        self.variant_calls = OneHotEncoder(
            variant_calls_ref, variant_calls_methy,
            variant_calls_snp, 1
        )
        self.variant_calls.encode_data()

        self.fake_letter = OneHotEncoder(
            other_chars_ref, other_chars_methy, 
            other_chars_snp, 1
        )
        self.fake_letter.encode_data()
        
    
    def test_vanilla(self):
        self.assertListEqual(self.four_letters.encoded_tensor, identity(4))

    def test_variants(self):
        self.assertListEqual(self.variant_calls.encoded_tensor, [[1,0,0,0] for x in range(4)])

    def test_fake_letter(self):
        self.assertListEqual(self.fake_letter.encoded_tensor, [[0, 0, 0, 0] for x in range(3)])
        
        

if __name__ == '__main__':
    unittest.main()