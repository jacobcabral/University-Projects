"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Jacob Cabral
ID:     190689750
Email:  cabr9750@mylaurier.ca
__updated__ = "2019-05-10"
------------------------------------------------------------------------
"""
from functions import count_frequency_value

file = open("numbers.txt")
num = int(input("Value to count: "))
count = count_frequency_value(file, num)
print("The value of {:.0f} appears {:.0f} time(s)".format(num,count))