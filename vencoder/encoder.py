from dataclasses import dataclass
from abc import ABC, abstractmethod

@dataclass
class Encoder:
    """Base constructor to encode one chromosome at a time
    reference_sequence:
        A string of A, C, G, T, and N (e.g. "AAAACCGTGTGTTGNN")
    variant_calls:
        A dictionary where keys are 1-based integer positions and values are tuples 
        or lists in the format (Reference, Alternate, Variant Call). E.g. ("A", ".", "0/0")
    """
    reference_sequence: str
    variant_calls: dict

    def __post_init__(self):
        # Promise 
        self.encoding = None

    @abstractmethod
    def encode_single_nucleotide(self, nt):
        pass

    def encode_data(self):
        '''Main logic of sequence encoding. Iterate through the reference sequence 
        and at each position, check if there is a variant call. If there is, encode the
        variant call. If not, encode the reference sequence.
        '''
        out = []
        
        for i, ref_nt in enumerate(self.reference_sequence):
            # Using one-based (VCF standard indexing)
            pos = i + 1

            if pos in self.variant_calls:
                # Find the variant call tuple, if there is a variant call
                vc = self.variant_calls[pos] # e.g. ('A', '.', '0/0')
                
                # Check that the variant call's idea of a reference
                # is the same as the fasta reference
                if not ((ref_nt == vc[0]) and (ref_nt in ['A', 'C', 'G', 'T'])):
                    raise Exception(f"Reference at position {pos} is {ref_nt} in fasta != {vc[0]} in VCF")
            else:
                # Construct a reference key
                vc = (ref_nt, ".", "0/0")

            out.append(self.encode_single_nucleotide(vc))
        self.encoding = out
