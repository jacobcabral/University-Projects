"""
------------------------------------------------------------------------
[Testing the function for q4]
------------------------------------------------------------------------
Author: Jacob Cabral
ID:     190689750
Email:  cabr9750@mylaurier.ca
__updated__ = "2019-10-10"
------------------------------------------------------------------------
"""
from a4_functions import quadrant

x_coordinate =int(input("Enter x coordinate: "))
y_coordinate = int(input("Enter y coordinate: "))

quadrant_value = quadrant(x_coordinate, y_coordinate)

print("\nThe coordinate ({:.0f},{:.0f}) lies in ".format(x_coordinate,y_coordinate) + quadrant_value)