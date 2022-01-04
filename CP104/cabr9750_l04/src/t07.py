"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Jacob Cabral
ID:     190689750
Email:  cabr9750@mylaurier.ca
__updated__ = "2019-10-02"
------------------------------------------------------------------------
"""
from functions import total_change

nickels = int(input("Enter number of nickels: "))
dimes = int(input("Enter number of dimes: "))
quarters = int(input("Enter number of quarters: "))
loonies = int(input("Enter number of loonies: "))
toonies = int(input("Enter number of toonies: "))
total = total_change(nickels, dimes, quarters, loonies, toonies)

print("Total amount: ${:.2f}".format(total))

