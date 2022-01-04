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
from a6_functions import is_prime

num = int(input("Please enter a positive integer: "))

while num < 0:
    num = int(input("\nPlease enter a positive integer: "))
    
result = is_prime(num)

if result == True:
    print("\n{:.0f} is a prime number".format(num))
else:
    print("\n{:.0f} is not a prime number".format(num))
