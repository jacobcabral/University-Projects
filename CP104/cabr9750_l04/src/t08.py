"""
------------------------------------------------------------------------
[testing function 8]
------------------------------------------------------------------------
Author: Jacob Cabral
ID:     190689750
Email:  cabr9750@mylaurier.ca
__updated__ = "2019-10-02"
------------------------------------------------------------------------
"""
from functions import computer_costs

computer_cost = float(input("Cost of each computer: "))
computers_bought = int(input("Number of computers bought: "))
commission_percent = float(input("Wholesaler commission: "))

pre_commission_cost, total_cost = computer_costs(computer_cost,computers_bought, commission_percent)

print("Cost of computers (no commission): ${:,.2f}".format(pre_commission_cost))
print("Cost of computers (total):         ${:,.2f}".format(total_cost))