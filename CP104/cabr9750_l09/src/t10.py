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
from functions import text_analyze

txt = str(input("Enter a string: "))
print()

uppr, lowr, dgts, whtspc = text_analyze(txt)

print("upper case letters: {:d}".format(uppr))
print("lower case letters: {:d}".format(lowr))
print("digits: {:d}".format(dgts))
print("whitespace characters: {:d}".format(whtspc))