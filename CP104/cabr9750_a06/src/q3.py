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
from a6_functions import factorial
num = int(input("Enter a positive integer: "))

result = factorial(num)

if result == -1:
    print("You did not enter a positive integer")
else:
    print("{:.0f}! = ".format(num), end = ' ')
    print(result)

