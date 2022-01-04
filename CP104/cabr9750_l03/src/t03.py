"""
------------------------------------------------------------------------
[prints the money made that day besed on the number of small and large dogs groomed]
------------------------------------------------------------------------
Author: Jacob Cabral
ID:     190689750
Email:  cabr9750@mylaurier.ca
__updated__ = "2019-09-25"
------------------------------------------------------------------------
"""
LARGE_DOG_PRICE = 75.00
SMALL_DOG_PRICE = 50.00

large_dogs_groomed = int(input("Number of large dogs groomed: "))
small_dogs_groomed = int(input("Number of small dogs groomed: "))


total_earned = (LARGE_DOG_PRICE * large_dogs_groomed) + (small_dogs_groomed * SMALL_DOG_PRICE)
print("Total earned for the day: ${:,.2f}.".format(total_earned))

