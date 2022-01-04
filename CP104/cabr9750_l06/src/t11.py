"""
------------------------------------------------------------------------
[testing for 11]
------------------------------------------------------------------------
Author: Jacob Cabral
ID:     190689750
Email:  cabr9750@mylaurier.ca
__updated__ = "2019-05-10"
------------------------------------------------------------------------
"""

from functions import retirement

age = int(input("Enter the worker's age: "))
salary = float(input("Enter the worker's salary: $"))
increase = float(input("Enter the yearly raise (%): "))
print()

retirement(age, salary, increase)