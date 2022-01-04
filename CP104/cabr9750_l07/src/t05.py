"""
------------------------------------------------------------------------
[testing the positive_statistics function]
------------------------------------------------------------------------
Author: Jacob Cabral
ID:     190689750
Email:  cabr9750@mylaurier.ca
__updated__ = "2019-10-30"
------------------------------------------------------------------------
"""
from functions import positive_statistics

minimum,maximum,total,average = positive_statistics()
print()
print("minimum: {:.2f}".format(minimum))
print("maximum: {:.2f}".format(maximum))
print("total: {:.2f}".format(total))
print("average: {:.2f}".format(average))
