from vencoder.encoder import Encoder

# How many alternate alleles
additive_dict = {
    "0/0": [0, 0, 0, 0],
    "0/1": [1, 1, 1, 1],
    "1/1": [2, 2, 2, 2],
    "1/2": [2, 2, 2, 2]
}

class AdditiveEncoder(Encoder):
    '''
    
    '''

    def encode_single_nucleotide(self, variant_call):
        vc = variant_call[2]
        return(additive_dict.get(vc, [0,0,0,0]))
       
        