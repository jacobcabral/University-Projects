"""
------------------------------------------------------------------------
[testing the lotto function]
------------------------------------------------------------------------
Author: Jacob Cabral
ID:     190689750
Email:  cabr9750@mylaurier.ca
__updated__ = "2019-05-10"
------------------------------------------------------------------------
"""
from functions import get_lotto_numbers

n = int(input("Number of values: "))
low = int(input("Low value: "))
high = int(input("High value: "))
numbers = get_lotto_numbers(n, low, high)
print("\nList entered: ", end = "")
print(numbers)  