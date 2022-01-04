"""
------------------------------------------------------------------------
[testing the find_frequent function]
------------------------------------------------------------------------
Author: Jacob Cabral
ID:     190689750
Email:  cabr9750@mylaurier.ca
__updated__ = "2019-11-15"
------------------------------------------------------------------------
"""
from a8_functions import find_frequent

userinput = str(input("Enter a string: "))

frequent_character = find_frequent(userinput)

print("The most frequent character(s) in the string is " , frequent_character)