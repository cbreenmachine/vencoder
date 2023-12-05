import unittest
from vencoder.onehot import OneHotEncoder
from testdata import *



class TestOneHotEncoder(unittest.TestCase):

    def setUp(self):
        self.alphabet = OneHotEncoder(alphabet_ref_seq, alphabet_ref_variant_calls)
        self.alphabet.encode_data()

        self.a_variant_calls = OneHotEncoder(a_ref_seq, a_variant_calls)
        self.a_variant_calls.encode_data()

        self.non_alphabet = OneHotEncoder(non_alphabet_ref_seq, non_alphabet_variant_calls)
        self.non_alphabet.encode_data()
        
    
    def test_alphabet(self):
        self.assertListEqual(
            self.alphabet.encoding, 
            alphabet_ref_expected_ohe
        )

    def test_a_variants(self):
        self.assertListEqual(
            self.a_variant_calls.encoding,
            a_expected_ohe
        )

    def test_fake_letter(self):
        self.assertListEqual(
            self.non_alphabet.encoding,
            non_alphabet_expected_ohe
        )
        
        

if __name__ == '__main__':
    unittest.main()