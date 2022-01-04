"""
------------------------------------------------------------------------
[testing the lumber function]
------------------------------------------------------------------------
Author: Jacob Cabral
ID:     190689750
Email:  cabr9750@mylaurier.ca
__updated__ = "2019-05-10"
------------------------------------------------------------------------
"""
from functions import lumber

b_min = int(input("Enter minimum value of the base: "))
b_max = int(input("Enter maximum value of the base: "))
b_inc = int(input("Enter increment in base value: "))
h_min = int(input("Enter minimum value of the height: "))
h_max = int(input("Enter maximum value of the height: "))
h_inc = int(input("Enter the increment in height value: "))

lumber(b_min, b_max, b_inc, h_min, h_max, h_inc)

