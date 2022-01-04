"""
------------------------------------------------------------------------
[testing function for 1]
------------------------------------------------------------------------
Author: Jacob Cabral
ID:     190689750
Email:  cabr9750@mylaurier.ca
__updated__ = "2019-05-10"
------------------------------------------------------------------------
"""
from a1_functions import max_three
x = float(input("Please enter your first number: "))
y = float(input("Please enter your second number: "))
z = float(input("Please enter your third number: "))

average = max_three(x, y, z)

print("The average of the two smaller values is {:.1f}".format(average))