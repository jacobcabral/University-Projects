"""
------------------------------------------------------------------------
[testing the get_int function]
------------------------------------------------------------------------
Author: Jacob Cabral
ID:     190689750
Email:  cabr9750@mylaurier.ca
__updated__ = "2019-10-30"
------------------------------------------------------------------------
"""
from functions import get_int

low = int(input("Enter the low value: "))
high = int(input("Enter the high value: "))

value = get_int(low, high)

print("Value: {:.0f}".format(value))