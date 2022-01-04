"""
------------------------------------------------------------------------
[shows a date_input in the format MM/DD/YY]
------------------------------------------------------------------------
Author: Jacob Cabral
ID:     190689750
Email:  cabr9750@mylaurier.ca
__updated__ = "2019-09-17"
------------------------------------------------------------------------
"""
date_input = int(input("Enter a date in the format MMDDYYYY: "))
year = date_input % 10000
date_no_year = (date_input - year) / 10000
day = int(date_no_year % 100)
month = int((date_no_year - day) / 100)
print(f"{day:02}/{month:02}/{year:04}")