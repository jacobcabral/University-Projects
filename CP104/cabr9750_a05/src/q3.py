"""
------------------------------------------------------------------------
[testing the function from 3]
------------------------------------------------------------------------
Author: Jacob Cabral
ID:     190689750
Email:  cabr9750@mylaurier.ca
__updated__ = "2019-10-10"
------------------------------------------------------------------------
"""
from a3_functions import base_price, time_discount, Length_discount


call_length = int(input("Length of call (minutes): "))
call_hour = int(input("Hour of call (24hour format): "))

if (call_hour > 24 or 0 > call_hour):
    print("\nPlease enter a valid time in the 24 hour format")
else:
    base_price = base_price(call_length)

    price_time_discount = time_discount(base_price, call_hour)

    price_length_discount = Length_discount(price_time_discount, call_length)

    print("\nTotal price of call: ${:.2f}".format(price_length_discount))