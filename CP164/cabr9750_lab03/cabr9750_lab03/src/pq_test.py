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
from Food_utilities import read_foods
from utilities import priority_queue_test

fv = open("foods.txt", mode = "r", encoding = "utf-8")

foods = read_foods(fv)

priority_queue_test(foods)
