"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Jacob Cabral
ID:      190689750
Email:   cabr9750@mylaurier.ca
__updated__ = "2020-03-11"
-------------------------------------------------------
"""

from functions import do_comparisons, letter_table
from Letter import Letter
from BST_linked import BST

DATA = "ETAOINSHRDLUCMPFYWGBVKJXZQ"

bst = BST()

for var in DATA:
    bst.insert(Letter(var))
    
file_variable = open("miserables.txt", "r")

do_comparisons(file_variable, bst)

file_variable.close()

letter_table(bst)