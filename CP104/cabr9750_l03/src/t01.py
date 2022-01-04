"""
------------------------------------------------------------------------
[converts degrees celsius to degrees fahrenheit]
------------------------------------------------------------------------
Author: Jacob Cabral
ID:     190689750
Email:  cabr9750@mylaurier.ca
__updated__ = "2019-09-25"
------------------------------------------------------------------------
"""
temperature_celsius = int(input("Temperature (C): "))
FREEZING_TEMPERATURE = 32
temperature_fahrenheit = (((9/5)*temperature_celsius)) + FREEZING_TEMPERATURE
print("Temperature (F): {:.0f}".format(temperature_fahrenheit))