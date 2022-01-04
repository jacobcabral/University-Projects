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
from functions import append_increment
file = open("numbers.txt","r+")
num = append_increment(file)
print("file 'numbers.txt' open and ready for reading and writing")
print(num)