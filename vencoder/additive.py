from vencoder.encoder import Encoder

# How many alternate alleles
additive_dict = {
    "0/0": [0, 0, 0, 0],
    "0/1": [1, 1, 1, 1],
    "1/1": [2, 2, 2, 2],
    "1/2": [2, 2, 2, 2]
}

class AdditiveModelEncoder(Encoder):
    '''
    
    '''

    def encode_single_nucleotide(self, variant_call):
        seq_encoding = additive_dict.get(variant_call, [0,0,0,0])
        pass
       
        