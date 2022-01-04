"""
------------------------------------------------------------------------
[testing function for diameter]
------------------------------------------------------------------------
Author: Jacob Cabral
ID:     190689750
Email:  cabr9750@mylaurier.ca
__updated__ = "2019-05-10"
------------------------------------------------------------------------
"""
from functions import diameter
radius = float(input("Enter radius: "))

final_radius = diameter(radius)

print("Diameter of circle: {:.2f}".format(final_radius))