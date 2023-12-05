


def identity(n):
    '''Matrix in list of lists form that had ones on diagonal, zeros elsewhere'''
    return [[1 if i==j else 0 for j in range(n)] for i in range(n)]


###############################################################
############# Vanilla letters (A,C,G,T) #######################
###############################################################
# Ensure that non-variants (0/0) get encoded properly. 
# Since we have one of each letter, we should get an identity matrix

alphabet_ref_seq = "ACGT"
alphabet_ref_variant_calls = [
    {1: ("A", ".", "0/0")},
    {2: ("C", ".", "0/0")},
    {3: ("G", ".", "0/0")},
    {4: ("T", ".", "0/0")}
]
alphabet_ref_expected_ohe = identity(4)


###############################################################
######## Variant call values (0/1, 1/1, 1/2) ##################
###############################################################
# reference, alternate, variant call
a_ref_seq = "AAAA"
a_variant_calls = [
    {1: ("A", "C", "0/0")},
    {2: ("A", "C", "0/1")},
    {3: ("A", "C", "1/1")},
    {4: ("A", "C", "1/2")}
]
a_expected_ohe = [[1,0,0,0]] * 4
a_expected_var = [[1,0,0,0]] * 4

###############################################################
######## Out of range nucleotides (N, ., R) ###################
###############################################################
non_alphabet_ref_seq = ".NR"
non_alphabet_variant_calls = [
    {1: (".", "C", "0/0")},
    {2: ("N", "C", "0/0")},
    {3: ("R", "C", "0/0")}
]
non_alphabet_expected_ohe = [[0,0,0,0]] * 3
non_alphabet_expected_var = [[0,0,0,0]] * 3