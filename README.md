# vencoder
Python module to encode variants in a variety of schemes.

# Motivation

Suppose you have some reference sequence (`A,A,C,C,G,G,T,T...`) and a list of variant calls (). In variant call parlance, 0/1 means there is one copy of the reference (denoted 0) and one copy of the alternate (denoted 1) allele. So, 0/0 means two copies of the reference (and is the most common occurence by a long shot). 


| 0-based | 1-based | Reference | Alternate | Variant Call |
|---------|---------|-----------|-----------|--------------|
| 0 | 1 | A | T | 0/1 |
| 1 | 2 | C | . | 0/0 |
| 2 | 3 | A | G | 1/1 |


