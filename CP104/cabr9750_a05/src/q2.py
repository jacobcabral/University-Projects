"""
------------------------------------------------------------------------
[testing the colour function]
------------------------------------------------------------------------
Author: Jacob Cabral
ID:     190689750
Email:  cabr9750@mylaurier.ca
__updated__ = "2019-05-10"
------------------------------------------------------------------------
"""
from a2_functions import pocket_color

num = int(input("Enter a pocket number: "))

color = pocket_color(num)

if (color != "ERROR"):
    print("\nThe selected pocket color is " + color +".")
else:
    print("\nThe pocket number entered is incorrect.")