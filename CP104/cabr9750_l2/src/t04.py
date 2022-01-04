"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Jacob Cabral
ID:     190689750
Email:  cabr9750@mylaurier.ca
__updated__ = "2019-09-18"
------------------------------------------------------------------------
"""
num_str = input("Enter number: ")
num_fl = float(num_str)
percent_discount = float(input("Enter percent: "))
percent_decimal = percent_discount/100

total_discount = num_fl*percent_decimal

num_fl = int(num_fl)

print("A {:.1f} percent discount on {:.0f} is {:.1f}".format(percent_discount,num_fl,total_discount))