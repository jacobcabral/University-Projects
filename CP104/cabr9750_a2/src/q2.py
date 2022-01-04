"""
------------------------------------------------------------------------
[calculates intrest and rounds off the result]
------------------------------------------------------------------------
Author: Jacob Cabral
ID:     190689750
Email:  cabr9750@mylaurier.ca
__updated__ = "2019-09-17"
------------------------------------------------------------------------
"""
import string
principal_amount = float(input("PLease enter the principal amount: "))
intrest_rate = float(input("Please enter the intrest rate as a decimal: "))
time = float(input("Enter the amount of time in years: "))
intrest_per_year = float(input("Enter the number of times the intrest is compounded per year: "))
compound_rate = intrest_rate/intrest_per_year
total_periods = intrest_per_year*time
total_balance = principal_amount * ((1.0+compound_rate)**total_periods)
total_balance = round(total_balance, 2)
total_balance = str(total_balance)
print("$"+ total_balance)


