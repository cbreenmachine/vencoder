from src.variant import VariantEncoder
from pandas import DataFrame, concat

variant_calls = ["0/0", "0/1", "1/1", "1/2"]
reference_letters = ["A", "C", "G", "T"]
alternate_letters = ["A", "C", "G", "T"]

ref_seq = ""
var_calls = {}

# 1-based keys representing position
pos = 1

for r in reference_letters:
    for a in alternate_letters:
        if not r == a:
            for c in variant_calls:
                ref_seq += r
                var_calls[pos] = (r, a, c)
                pos += 1


my_encoder = VariantEncoder(ref_seq, var_calls)
my_encoder.encode_data()


a = DataFrame(var_calls).transpose()

one_based_ix = [x for x in range(1, len(var_calls)+1)]
b = DataFrame(my_encoder.encoding, index=one_based_ix)

out_df = concat((a, b), axis=1)
out_df.columns = ['Reference', 'Alternate', 'VariantCall', 'A', 'C', 'G', 'T']
out_df.to_csv("toy-data.csv", index=False)