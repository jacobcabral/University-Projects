"""
------------------------------------------------------------------------
[testing analysis_file]
------------------------------------------------------------------------
Author: Jacob Cabral
ID:     190689750
Email:  cabr9750@mylaurier.ca
__updated__ = "2019-11-23"
------------------------------------------------------------------------
"""
from a9_functions import analysis_file
f = open("text.txt","r")
uppercase,lowercase,digits,whitespace = analysis_file(f)

text = "{:.0f},{:.0f},{:.0f},{:.0f}".format(uppercase,lowercase,digits,whitespace)

fv = open("output_q3.txt","w+")
fv.write(text)
fv.close