"""
------------------------------------------------------------------------
[calculates the number of children that will get baloons at a party]
------------------------------------------------------------------------
Author: Jacob Cabral
ID:     190689750
Email:  cabr9750@mylaurier.ca
__updated__ = "2019-09-24"
------------------------------------------------------------------------
"""
number_of_balloons = int(input("Enter number of balloons: "))
number_of_children = int(input("Enter number of children: "))

balloons_recived = number_of_balloons//number_of_children
balloons_not_received = number_of_balloons%number_of_children

print("Each child will receive",balloons_recived,"balloons")
print("Balloons that won't be distributed:",balloons_not_received)