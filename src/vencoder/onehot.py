from .encoder import Encoder

# Define the standard 
ohe_dict = {
    'A': [1, 0, 0, 0],
    'C': [0, 1, 0, 0],
    'G': [0, 0, 1, 0],
    'T': [0, 0, 0, 1]
}

class OneHotEncoder(Encoder):
    '''Standard method of 

    '''

    def encode_nucleotide(self, nt):
        return(ohe_dict.get(nt, [0, 0, 0, 0]))

    def encode_data(self):

        out = []
        for x in self.ref_seq:
            out.append(self.encode_nucleotide(x))
        
        self.encoded_tensor = out
