"""
------------------------------------------------------------------------
[testing the pyramid function]
------------------------------------------------------------------------
Author: Jacob Cabral
ID:     190689750
Email:  cabr9750@mylaurier.ca
__updated__ = "2019-10-02"
------------------------------------------------------------------------
"""
from functions import square_pyramid

base = float(input("Length of base: "))
height = float(input("Perpendicular height of pyramid: "))

sh, a, v = square_pyramid(base, height)

print("Slant height of square pyramid: {:.2f}".format(sh))
print("Area of square pyramid: {:.2f}".format(a))
print("Volume of square pyramid: {:.2f}".format(v))

