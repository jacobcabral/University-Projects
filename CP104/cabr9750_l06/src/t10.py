"""
------------------------------------------------------------------------
[testing treadmill]
------------------------------------------------------------------------
Author: Jacob Cabral
ID:     190689750
Email:  cabr9750@mylaurier.ca
__updated__ = "2019-05-10"
------------------------------------------------------------------------
"""
from functions import treadmill
burnt_per_minute = float(input("Enter calories burned per minute: "))
start = int(input("Enter beginning number of minutes: "))
end = int(input("Enter ending number of minutes: "))
inc = int(input("Enter the increment in minutes: "))

treadmill(burnt_per_minute, start, end, inc)



