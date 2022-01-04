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
from functions import do_comparisons, comparison_total
from Letter import Letter
from BST_linked import BST


DATA1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DATA2 = "MFTCJPWADHKNRUYBEIGLOQSVXZ"
DATA3 = "ETAOINSHRDLUCMPFYWGBVKJXZQ"

BST1 = BST()
BST2 = BST()
BST3 = BST()

for var in DATA1:
    BST1.insert(Letter(var))

for var in DATA2:
    BST2.insert(Letter(var))

for var in DATA3:
    BST3.insert(Letter(var))
    
file_variable = open("miserables.txt", "r")
do_comparisons(file_variable, BST1)
file_variable.close()

file_variable = open("miserables.txt", "r")
do_comparisons(file_variable, BST2)
file_variable.close()

file_variable = open("miserables.txt", "r")
do_comparisons(file_variable, BST3)
file_variable.close()

total1 = comparison_total(BST1)
total2 = comparison_total(BST2)
total3 = comparison_total(BST3)

print("Comparing by order: ABCDEFGHIJKLMNOPQRSTUVWXYZ")
print("Total Comparisons: {:,d}".format(total1))

print("Comparing by order: MFTCJPWADHKNRUYBEIGLOQSVXZ")
print("Total Comparisons: {:,d}".format(total2))

print("Comparing by order: ETAOINSHRDLUCMPFYWGBVKJXZQ")
print("Total Comparisons: {:,d}".format(total3))
