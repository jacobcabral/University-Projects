"""
------------------------------------------------------------------------
[testing the population_growth function]
------------------------------------------------------------------------
Author: Jacob Cabral
ID:     190689750
Email:  cabr9750@mylaurier.ca
__updated__ = "2019-10-30"
------------------------------------------------------------------------
"""
from functions import population_growth

target = int(input("Target population: "))
current = int(input("Current population: "))
rate = float(input("Growth rate (%): "))

years = population_growth(target,current,rate)

print("\nYears to target: {:.0f}".format(years))
