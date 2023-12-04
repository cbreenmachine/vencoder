from dataclasses import dataclass
from abc import ABC, abstractmethod
from pandas import DataFrame

# from typing import Union, List

# Better to encode all letters and then "digitize" 
# or keep it as is and iterate through

@dataclass
class Encoder:
    """Base constructor to encode one chromosome at a time"""
    ref_seq: str
    methy_data: dict
    snp_data: dict
    window: int = 2000

    def __post_init__(self):

        # Check 
        self.encoded_tensor = None

        # if isinstance(self.methy_data, list):
        #     self.methy_df = DataFrame(self.methy_data, 
        #                                  columns = ['pos', 'methylated', 'coverage']).set_index('pos')
        # else:
        #     self.methy_df = self.snp_data

        if isinstance(self.snp_data, list):
            self.snp_df = DataFrame(self.snp_data, 
                                         columns = ['pos', 'reference', 'alternate', 'variant_call']).set_index('pos')
        else:
            self.snp_df = self.snp_data
    
    @abstractmethod
    def encode_data(self):
        pass




