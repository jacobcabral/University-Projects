"""
------------------------------------------------------------------------
[testing the function for 8]
------------------------------------------------------------------------
Author: Jacob Cabral
ID:     190689750
Email:  cabr9750@mylaurier.ca
__updated__ = "2019-10-09"
------------------------------------------------------------------------
"""
from functions import roman_numeral

n = int(input("Enter a number from 1 to 10: "))

numeral = roman_numeral(n)

if (numeral != None):
    print("The Roman numeral equivalent of {:.0f} is ".format(n) + numeral)
else:
    print("{:.0f} does not have a Roman Numeral equivalent".format(n))
    

    

