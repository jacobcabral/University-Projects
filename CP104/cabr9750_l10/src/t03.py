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
from functions import customer_best
file = open("customers.txt")
result = customer_best(file)
print("Find the customer with the largest balance: ")
print(result)