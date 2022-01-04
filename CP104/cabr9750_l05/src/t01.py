"""
------------------------------------------------------------------------
[testing functions for 1]
------------------------------------------------------------------------
Author: Jacob Cabral
ID:     190689750
Email:  cabr9750@mylaurier.ca
__updated__ = "2019-10-09"
------------------------------------------------------------------------
"""
from functions import magic_date
print("Enter a date.")
day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year (2 digits): "))

magic = magic_date(day, month, year)

if (magic == True):
    print("\n{:.0f}/{:.0f}/{:.0f} is a magic date.".format(day,month,year))
else:
    print("\n{:.0f}/{:.0f}/{:.0f} is not a magic date.".format(day,month,year))
    