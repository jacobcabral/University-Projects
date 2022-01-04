"""
-------------------------------------------------------
[t05]
-------------------------------------------------------
Author:  Jacob Cabral
ID:      190689750
Email:   cabr9750@mylaurier.ca
__updated__ = "2020-01-23"
-------------------------------------------------------
"""
from Food_utilities import by_origin, read_foods, average_calories, calories_by_origin,food_table,food_table,food_search

fv = open("foods.txt", "r", encoding="utf-8")
foods = read_foods(fv)

origin = 1
max_cals = 0
is_veg = False
results = food_search(foods, origin, max_cals, is_veg)
print(results)

