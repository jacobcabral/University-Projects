"""
------------------------------------------------------------------------
[testing the is_word_chain function]
------------------------------------------------------------------------
Author: Jacob Cabral
ID:     190689750
Email:  cabr9750@mylaurier.ca
__updated__ = "2019-11-15"
------------------------------------------------------------------------
"""
from a8_functions import is_word_chain

chain = ['camel', 'leopard', 'dog', 'giraffe', 'elephant']

result = is_word_chain(chain)

if result == True:
    print("The list contains a word chain")
else:
    print("The list does not contain a word chain")