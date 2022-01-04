"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Jacob Cabral
ID:     190689750
Email:  cabr9750@mylaurier.ca
__updated__ = "2019-05-10"
------------------------------------------------------------------------
"""
from functions import file_copy_n

fv_1 = open("words.txt", "r")
fv_2 = open("new_words.txt", "a")

n = int(input("Copying 'words.txt' to 'new_words.txt'\nNumber of lines to copy: "))

file_copy_n(fv_1, fv_2, n)