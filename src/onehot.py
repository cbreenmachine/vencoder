from .encoder import Encoder

# Define the standard 
ohe_dict = {
    'A': [1, 0, 0, 0],
    'C': [0, 1, 0, 0],
    'G': [0, 0, 1, 0],
    'T': [0, 0, 0, 1]
}

class OneHotEncoder(Encoder):
    '''Standard method of encoding nucleotides

    '''

    def encode_single_nucleotide(self, variant_call):
        # Only care about the first letter
        nt = variant_call[0]
        return(ohe_dict.get(nt, [0, 0, 0, 0]))

