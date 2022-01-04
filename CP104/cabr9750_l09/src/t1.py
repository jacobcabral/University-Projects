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
from functions import is_hydroxide

chemical = str(input("Enter a chemical formula: "))
hydroxide = is_hydroxide(chemical)

if hydroxide:
    print("{} is a hydroxide.".format(chemical))
else:
    print("{} is not a hydroxide.".format(chemical))