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
breakfast_cost = float(input("Enter cost of breakfast: "))
lunch_cost = float(input("Enter the cost of lunch: "))
dinner_cost = float(input("Enter the cost of supper: "))

total_cost = breakfast_cost+lunch_cost+dinner_cost

print("Meal         Cost")
print("Breakfast    ${:6.2f}".format(breakfast_cost))
print("Lunch        ${:6.2f}".format(lunch_cost))
print("Supper       ${:6.2f}".format(dinner_cost))
print("Total        ${:6.2f}".format(total_cost))