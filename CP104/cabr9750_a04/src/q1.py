"""
------------------------------------------------------------------------
[calculates federal and provincal tax tax based on the user's income]
------------------------------------------------------------------------
Author: Jacob Cabral
ID:     190689750
Email:  cabr9750@mylaurier.ca
__updated__ = "2019-10-1"
------------------------------------------------------------------------
"""
from q1_functions import calc_federal_tax, calc_prov_tax

income = float(input("Enter your income: $ "))

prov_tax = calc_prov_tax(income)
federal_tax = calc_federal_tax(income)

total_tax = prov_tax + federal_tax

print("\nYour total tax liability is: $ {:.0f}".format(total_tax))
print("[details federal tax is: $ {:.0f}, state tax is: $ {:.0f}]".format(federal_tax,prov_tax))