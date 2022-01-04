"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  your name
ID:      your id
Email:   your email
__updated__ = "2020-01-27"
-------------------------------------------------------
"""
from utilities import queue_test
from Food_utilities import read_foods

fv = open("foods.txt", mode = "r", encoding = "utf-8")

foods = read_foods(fv)

queue_test(foods)

