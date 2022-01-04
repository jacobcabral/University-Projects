"""
------------------------------------------------------------------------
[calculates intrest with the inputted principal amount, yearly intrest rate and number of years]
------------------------------------------------------------------------
Author: Jacob Cabral
ID:     190689750
Email:  cabr9750@mylaurier.ca
__updated__ = "2019-09-25"
------------------------------------------------------------------------
"""
principal_amount = float(input("Mortgage principal ($): ")) #p
number_of_years = int(input("Number of years: "))
number_of_months = number_of_years * 12 #n
yearly_intrest = float(input("Yearly interest rate (%): "))
monthly_intrest = (yearly_intrest/100)/12  #i

percent_growth = ((1+ monthly_intrest)** number_of_months)


monthly_payments = principal_amount *((monthly_intrest * percent_growth)/(percent_growth - 1))

print("The monthly payments are: ${:,.2f}".format(monthly_payments))





