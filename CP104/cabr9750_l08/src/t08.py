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
from functions import linear_search

values = [94, 96, -22, -79, -28, -26, -50, 71, 24, -32]
print("Values: {}".format(values))
print()

print("Index of {}: {}".format(-22, linear_search(values, -22)))
print("Index of {}: {}".format(71, linear_search(values, 71)))
print("Index of {}: {}".format(99, linear_search(values, 99)))