"""
------------------------------------------------------------------------
[testing find_median]
------------------------------------------------------------------------
Author: Jacob Cabral
ID:     190689750
Email:  cabr9750@mylaurier.ca
__updated__ = "2019-11-23"
------------------------------------------------------------------------
"""
from a9_functions import find_median
f = open("numbers.txt","r")
numbers,median = find_median(f)

text = "["
for i in range(len(numbers) - 1):
    text+=str(numbers[i]) + "+"
text+=str(numbers[-1])
text+="]="+ str(median)

fv = open("output_q2.txt","w+")
fv.write(text)
fv.close
