"""
------------------------------------------------------------------------
[testing the function for 12]
------------------------------------------------------------------------
Author: Jacob Cabral
ID:     190689750
Email:  cabr9750@mylaurier.ca
__updated__ = "2019-10-09"
------------------------------------------------------------------------
"""
from functions import pay_raise

status = str(input("Status: "))
years = int(input("Years: "))
salary= int(input("Salary: "))

new_salary = pay_raise(status, years, salary)

print("\nNew Salary: ${:.2f}".format(new_salary))

