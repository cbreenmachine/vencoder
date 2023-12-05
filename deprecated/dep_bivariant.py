from dataclasses import dataclass
from abc import ABC, abstractmethod
from pandas import DataFrame
from .base import Encoder

def one_in_ix(ix, length = 10):
    out = [0] * length
    out[ix] = 1
    return(out)
    

bivariant_dict = {

    # Cover the As first
    ('A', '.', '0/0'): one_in_ix(0), #A/A
    ('A', 'C', '0/1'): one_in_ix(1), #A/C
    ('C', 'A', '0/1'): one_in_ix(1),
    ('A', 'G', '0/1'): one_in_ix(2), #A/G
    ('G', 'A', '0/1'): one_in_ix(2),
    ('A', 'T', '0/1'): one_in_ix(3), #A/T
    ('T', 'A', '0/1'): one_in_ix(3),

    # Occasionally, ref/alternate 
    ('C', '.', '0/0'): one_in_ix(4), #C/C
    ('C', 'G', '0/1'): one_in_ix(5), #C/G
    ('G', 'C', '0/1'): one_in_ix(5),
    ('C', 'T', '0/1'): one_in_ix(6), #C/T
    ('T', 'C', '0/1'): one_in_ix(6),

    ('G', '.', '0/0'): one_in_ix(7), #G/G
    ('G', 'T', '0/1'): one_in_ix(8), #G/T
    ('T', 'G', '0/1'): one_in_ix(8),

    ('T', 'T', '0/1'): one_in_ix(9), #T/T
}



class BivariantEncoder(Encoder):

    def encode_nucleotide(self, key):
        '''Given a tuple in the form ("A", "C", "0/1") computes the
        warm encoding for a variant.
        '''
        return(bivariant_dict.get(key, [0]*10))

    # Could refactor this...
    def encode_data(self):
        out = []
        
        for i, nt in enumerate(self.ref_seq):
            pos = i + 1

            if pos in self.snp_df.index:
                row = self.snp_df.loc[pos]
                key = (row['reference'], row['alternate'], row['variant_call'])
            else:
                # Get reference (the case 99% of the time)
                key = (nt, ".", "0/0")

            out.append(self.encode_nucleotide(key))

        self.encoded_tensor = out
                
                
       
        