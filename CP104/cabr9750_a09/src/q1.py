"""
------------------------------------------------------------------------
[testing sum_numbers]
------------------------------------------------------------------------
Author: Jacob Cabral
ID:     190689750
Email:  cabr9750@mylaurier.ca
__updated__ = "2019-11-23"
------------------------------------------------------------------------
"""
from a9_functions import sum_numbers
f = open("myfile.txt","r")

numbers, total = sum_numbers(f)

text = "["
for i in range(len(numbers) - 1):
    text+=str(numbers[i]) + "+"
text+=str(numbers[-1])
text+="]="+ str(total)

fv = open("output_q1.txt","w+")
fv.write(text)
fv.close
