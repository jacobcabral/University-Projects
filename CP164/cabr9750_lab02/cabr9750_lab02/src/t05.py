"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  your name
ID:      your id
Email:   your email
__updated__ = "2020-01-20"
-------------------------------------------------------
"""
from Food_utilities import read_food
from Stack_array import Stack

file = open("foods.txt", "r", encoding="utf-8")
s = Stack()

for line in file:
    s.push(read_food(line))
    
for element in s:
    print(element,end="\n\n")
