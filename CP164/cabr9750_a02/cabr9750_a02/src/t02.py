"""
-------------------------------------------------------
[t02]
-------------------------------------------------------
Author:  Jacob Cabral
ID:      190689750
Email:   cabr9750@mylaurier.ca
__updated__ = "2020-01-23"
-------------------------------------------------------
"""
from Food_utilities import by_origin, read_foods, average_calories
fv = open("foods.txt", "r", encoding="utf-8")
foods = read_foods(fv)

v = average_calories(foods)
print(v)