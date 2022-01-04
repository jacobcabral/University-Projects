"""
-------------------------------------------------------
[t01]
-------------------------------------------------------
Author:  Jacob Cabral
ID:      190689750
Email:   cabr9750@mylaurier.ca
__updated__ = "2020-01-23"
-------------------------------------------------------
"""
from Food_utilities import by_origin, read_foods

fv = open("foods.txt", "r", encoding="utf-8")
foods = read_foods(fv)
origin = int(input("Enter a food origin(0-11): "))

origins = by_origin(foods, origin)
for food in origins:
    print(food,end="\n\n")

fv.close()