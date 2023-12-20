from vencoder.onehot import OneHotEncoder
from vencoder.variant import VariantEncoder
from vencoder.additive import AdditiveEncoder
from pandas import DataFrame, concat

ref_seq = "ATCCGTGT"
var_calls = {
    1: ('A', '.', '0/0'),
    2: ('T', 'A', '0/1'),
    3: ('C', '.', '0/0'),
    4: ('C', '.', '0/0'),
    5: ('G', '.', '0/0'),
    6: ('T', '.', '0/0'),
    7: ('G', 'C', '1/1'),
    8: ('T', '.', '0/0'),
} #1-based


# One-hot encoding
ohe = OneHotEncoder(ref_seq, var_calls)
ohe.encode_data()

# Variant encoder
variant = VariantEncoder(ref_seq, var_calls)
variant.encode_data()

# Variant encoder
mask = AdditiveEncoder(ref_seq, var_calls)
mask.encode_data()


def construct_dataframe(encoding, var_calls):
    '''Helper function to convert outputs to a tidy dataframe'''

    # Variant calls become their own dataframe
    vc_df = DataFrame(var_calls).transpose()
    vc_df.columns = ['Reference', 'Alternate', 'VariantCall']
        
    # Need to construct a one-based index
    one_based_ix = [x+1 for x in range(vc_df.shape[0])]
    encoding_df = DataFrame(encoding, index=one_based_ix)
    encoding_df.columns = ['A', 'C', 'G', 'T']

    # Join and put in column names
    out_df = concat((vc_df, encoding_df), axis=1)

    return(out_df)

ohe_df = construct_dataframe(ohe.encoding, var_calls)
var_df = construct_dataframe(variant.encoding, var_calls)
mask_df = construct_dataframe(mask.encoding, var_calls)

ohe_df.to_csv("demo/paper_data_one_hot_encoding.csv", index=False)
var_df.to_csv("demo/paper_data_variant_encoding.csv", index=False)
mask_df.to_csv("demo/paper_data_mask_encoding.csv", index=False)
