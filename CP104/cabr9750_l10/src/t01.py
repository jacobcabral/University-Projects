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
from functions import customer_record

file = open("customers.txt")
print("Find record n")
n = int(input("Enter a record number: "))
result = customer_record(file, n)
print(result)