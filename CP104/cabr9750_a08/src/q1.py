"""
------------------------------------------------------------------------
[testing the sum_digit_string funcitons]
------------------------------------------------------------------------
Author: Jacob Cabral
ID:     190689750
Email:  cabr9750@mylaurier.ca
__updated__ = "2019-11-15"
------------------------------------------------------------------------
"""
from a8_functions import sum_digit_string

my_str = str(input("Enter a string with single digit numbers: "))

total = sum_digit_string(my_str)

print("The total value of the digits in the string is {:.0f}".format(total))
