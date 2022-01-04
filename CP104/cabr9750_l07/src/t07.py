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
from functions import meal_costs
breakfast, Lunch, supper, grand_total = meal_costs()
print("Total:")
print("Breakfast:   $ {:.2f}".format(breakfast))
print("Lunch:       $ {:.2f}".format(Lunch))
print("Supper:      $ {:.2f}".format(supper))
print()
print("Grand total: ${:.2f}".format(grand_total))