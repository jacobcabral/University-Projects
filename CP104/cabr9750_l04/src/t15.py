"""
------------------------------------------------------------------------
[testing function for q15]
------------------------------------------------------------------------
Author: Jacob Cabral
ID:     190689750
Email:  cabr9750@mylaurier.ca
__updated__ = "2019-10-02"
------------------------------------------------------------------------
"""
from functions import time_split

initial_seconds = int(input("Number of seconds: "))

days, hours, minutes, seconds = time_split(initial_seconds)

print("Days: {:.0f}, Hours: {:.0f}, Minutes: {:.0f}, Seconds: {:.0f}".format(days,hours,minutes,seconds))
