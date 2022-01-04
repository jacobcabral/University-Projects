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
second_entry = int(input("Enter the number of seconds: "))
hours = second_entry//3600
minutes = (second_entry%3600)//60
seconds = ((second_entry%3600)%60)

print("There are {:.0f} hours, {:.0f} minutes and {:.0f} seconds in {:.0f} seconds".format(hours,minutes,seconds,second_entry))