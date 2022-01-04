"""
------------------------------------------------------------------------
[Testing the hi lo function]
------------------------------------------------------------------------
Author: Jacob Cabral
ID:     190689750
Email:  cabr9750@mylaurier.ca
__updated__ = "2019-10-30"
------------------------------------------------------------------------
"""
from functions import hi_lo_game
high = int(input("Enter high"))
count = hi_lo_game(high)

print("You made {:.0f} guesses".format(count))