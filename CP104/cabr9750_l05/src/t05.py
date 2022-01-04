"""
------------------------------------------------------------------------
[testing the function for 5]
------------------------------------------------------------------------
Author: Jacob Cabral
ID:     190689750
Email:  cabr9750@mylaurier.ca
__updated__ = "2019-10-09"
------------------------------------------------------------------------
"""
from functions import is_leap

year = int(input("Enter a year (>0): "))

result = is_leap(year)

if (result == True):
    print("{:.0f} is a leap year".format(year))
else:
    print("{:.0f} is not a leap year".format(year))
