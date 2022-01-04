"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Jacob Cabral
ID:      190689750
Email:   cabr9750@mylaurier.ca
__updated__ = "2020-02-26"
-------------------------------------------------------
"""
from List_array import List
from Food_utilities import read_foods
from Food import Food

fv = open("foods.txt", mode = "r", encoding = "utf-8")

foods = read_foods(fv)

empty = list()

print(foods.is_identical(empty))
foods.remove_many()
foods.__getitem__()
foods.clean()

