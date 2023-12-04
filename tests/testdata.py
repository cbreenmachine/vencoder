


def identity(n):
    '''Matrix in list of lists form that had ones on diagonal, zeros elsewhere'''
    return [[1 if i==j else 0 for j in range(n)] for i in range(n)]


###############################################################
############# Vanilla letters (A,C,G,T) #######################
###############################################################
four_letters_ref = "ACGT"
four_letters_snp = [
    (1, "A", ".", "0/0"),
    (2, "C", ".", "0/0"),
    (3, "G", ".", "0/0"),
    (4, "T", ".", "0/0")
]
four_letters_methy = [(x+1, 0, 1) for x in range(4)]


###############################################################
######## Variant call values (0/1, 1/1, 1/2) ##################
###############################################################
# reference, alternate, variant call
variant_calls_ref = "AAAA"
variant_calls_snp = [
    (1, "A", "C", "0/0"),
    (2, "A", "C", "0/1"),
    (3, "A", "C", "1/1"),
    (4, "A", "C", "1/2")
]
# No need to alter this
variant_calls_methy = [(x+1, 0, 1) for x in range(4)]


###############################################################
######## Out of range nucleotides (N, ., R) ###################
###############################################################
other_chars_ref = ".NR"
other_chars_snp = [
    (1, ".", "C", "0/0"),
    (2, "N", "C", "0/0"),
    (3, "R", "C", "0/0")
]
# No need to alter this
other_chars_methy = [(x+1, 0, 1) for x in range(3)]