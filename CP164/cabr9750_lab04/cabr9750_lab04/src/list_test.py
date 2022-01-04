"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Jacob Cabral
ID:      190689750
Email:   cabr9750@mylaurier.ca
__updated__ = "2020-02-03"
-------------------------------------------------------
"""
from List_array import List
from Food_utilities import read_foods
from utilities import list_test

fv = open("foods.txt", mode = "r", encoding = "utf-8")

foods = read_foods(fv)

list_test(foods)
