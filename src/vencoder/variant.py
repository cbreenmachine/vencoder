from dataclasses import dataclass
from abc import ABC, abstractmethod
from pandas import DataFrame
from .base import Encoder

variant_dict = {
    # Most of the time, reference homozygote
    ('A', '.', '0/0'): [1, 0, 0, 0],
    ('A', 'C', '0/0'): [1, 0, 0, 0],
    ('A', 'G', '0/0'): [1, 0, 0, 0],
    ('A', 'T', '0/0'): [1, 0, 0, 0],
    
    ('C', '.', '0/0'): [0, 1, 0, 0],
    ('C', 'A', '0/0'): [0, 1, 0, 0],
    ('C', 'G', '0/0'): [0, 1, 0, 0],
    ('C', 'T', '0/0'): [0, 1, 0, 0],

    ('G', '.', '0/0'): [0, 0, 1, 0],
    ('G', 'A', '0/0'): [0, 0, 1, 0],
    ('G', 'C', '0/0'): [0, 0, 1, 0],
    ('G', 'T', '0/0'): [0, 0, 1, 0],
    
    ('T', '.', '0/0'): [0, 0, 0, 1],
    ('T', 'A', '0/0'): [0, 0, 0, 1],
    ('T', 'C', '0/0'): [0, 0, 0, 1],
    ('T', 'G', '0/0'): [0, 0, 0, 1],

    # Occasionally, ref/alternate 
    ('A', 'C', '0/1'): [0.5, 0.5, 0, 0],
    ('A', 'G', '0/1'): [0.5, 0, 0.5, 0],
    ('A', 'T', '0/1'): [0.5, 0, 0, 0.5],

    ('C', 'A', '0/1'): [0.5, 0.5, 0, 0],
    ('C', 'G', '0/1'): [0, 0.5, 0.5, 0],
    ('C', 'T', '0/1'): [0, 0.5, 0, 0.5],

    ('G', 'A', '0/1'): [0.5, 0, 0.5, 0],
    ('G', 'C', '0/1'): [0, 0.5, 0.5, 0],
    ('G', 'T', '0/1'): [0, 0.5, 0, 0.5],

    ('T', 'A', '0/1'): [0.5, 0, 0, 0.5],
    ('T', 'C', '0/1'): [0, 0.5, 0, 0.5],
    ('T', 'G', '0/1'): [0, 0, 0.5, 0.5],

    # Sometime Alt/Alt
    ('C', 'A', '1/1'): [1, 0, 0, 0],
    ('G', 'A', '1/1'): [1, 0, 0, 0],
    ('T', 'A', '1/1'): [1, 0, 0, 0],

    ('A', 'C', '1/1'): [0, 1, 0, 0],
    ('G', 'C', '1/1'): [0, 1, 0, 0],
    ('T', 'C', '1/1'): [0, 1, 0, 0],

    ('A', 'G', '1/1'): [0, 0, 1, 0],
    ('C', 'G', '1/1'): [0, 0, 1, 0],
    ('T', 'G', '1/1'): [0, 0, 1, 0],

    ('A', 'T', '1/1'): [0, 0, 0, 1],
    ('C', 'T', '1/1'): [0, 0, 0, 1],
    ('G', 'T', '1/1'): [0, 0, 0, 1],

    # Super rare, but occasionally 1/2
    ('A', 'C', '1/2'): [0, 0.5, 0.25, 0.25],
    ('A', 'G', '1/2'): [0, 0.25, 0.5, 0.25],
    ('A', 'T', '1/2'): [0, 0.25, 0.25, 0.5],

    ('C', 'A', '1/2'): [0.5, 0, 0.25, 0.25],
    ('C', 'G', '1/2'): [0.25, 0, 0.5, 0.25],
    ('C', 'T', '1/2'): [0.25, 0, 0.25, 0.5],

    ('G', 'A', '1/2'): [0.5, 0.25, 0, 0.25],
    ('G', 'C', '1/2'): [0.25, 0.5, 0, 0.25],
    ('G', 'T', '1/2'): [0.25, 0.25, 0, 0.5],

    ('T', 'A', '1/2'): [0.5, 0.25, 0.25, 0],
    ('T', 'C', '1/2'): [0.25, 0.5, 0.25, 0],
    ('T', 'G', '1/2'): [0.25, 0.25, 0.5, 0]
}


class VariantEncoder(Encoder):

    def encode_nucleotide(self, key):
        '''Given a tuple in the form ("A", "C", "0/1") computes the
        warm encoding for a variant.
        '''
        return(variant_dict.get(key, [0, 0, 0, 0]))

    def encode_data(self):
        out = []
        
        for i, nt in enumerate(self.ref_seq):
            pos = i + 1

            if pos in self.snp_df.index:
                row = self.snp_df.loc[pos]
                key = (row['reference'], row['alternate'], row['variant_call'])

                if (nt in ['A', 'C', 'G', 'T']) and (key[0] in ['A', 'C', 'G', 'T']):
                    if (nt != key[0]):
                        raise Exception(f"Reference at pos {pos} is {nt} in fasta != {key[0]} in VCF")
            else:
                # Get reference (the case 99% of the time)
                key = (nt, ".", "0/0")

            out.append(self.encode_nucleotide(key))

        self.encoded_tensor = out
                
                
       
        