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
from functions import symmetric_difference
source1 = [10, 3, 10, 3, 1]
source2 = [8, 2, 7, 3, 6, 10, 32, 99]

target = symmetric_difference(source1, source2)
print("Difference: ")
print(target)