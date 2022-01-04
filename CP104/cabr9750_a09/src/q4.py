"""
------------------------------------------------------------------------
[testing the serial number functions]
------------------------------------------------------------------------
Author: Jacob Cabral
ID:     190689750
Email:  cabr9750@mylaurier.ca
__updated__ = "2019-11-23"
------------------------------------------------------------------------
"""
from a9_functions import valid_sn_file, valid_sn
f = open("serial_number.txt","r")
g = open("serial_number_valid.txt","w+")
h = open("serial_number_invalid.txt","w+")
valid_sn_file(f,g,h)
