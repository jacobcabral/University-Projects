"""
------------------------------------------------------------------------
[converts inches to metres and displays it]
------------------------------------------------------------------------
Author: Jacob Cabral
ID:     190689750
Email:  cabr9750@mylaurier.ca
__updated__ = "2019-09-12"
------------------------------------------------------------------------
"""

INCHES_TO_METRES = 0.0254
#grab user input and assign it to a float value
inches_input = float(input("Please enter the number of inches: "))
#calculate the total number of metres and display it
total_metres = (inches_input*INCHES_TO_METRES)
print(inches_input, "In height is equivalent to", total_metres, "metres.")