"""
------------------------------------------------------------------------
[testing sum_even function]
------------------------------------------------------------------------
Author: Jacob Cabral
ID:     190689750
Email:  cabr9750@mylaurier.ca
__updated__ = "2019-10-23"
------------------------------------------------------------------------
"""
from functions import sum_even

num = int(input("Enter a number: "))
total = sum_even(num)

print("The sum of all even numbers from 2 to", num , "is" , total)