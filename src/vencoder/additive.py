from dataclasses import dataclass
from abc import ABC, abstractmethod
from pandas import DataFrame
from .base import Encoder

# How many alt alleles
additive_dict = {
    "0/0": 0,
    "0/1": 1,
    "1/1": 2,
    "1/2": 2
}


class AdditiveEncoder(Encoder):

    def encode_num_alt_alleles(self, vc):
        '''Given variant call (e.g. "0/1"), returns the SNP mask for a variant'''
        return(additive_dict.get(vc, 0))

    # Could refactor this...
    def encode_data(self):
        out = []
        
        for i, nt in enumerate(self.ref_seq):
            pos = i + 1

            if pos in self.snp_df.index:
                vc = self.snp_df.loc[pos]['variant_call']
            else:
                # Get reference (the case 99% of the time)
                vc = "0/0"

            out.append(self.encode_num_alt_alleles(vc))

        self.encoded_tensor = out
                
                
       
        