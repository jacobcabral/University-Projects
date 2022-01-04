"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Jacob Cabral
ID:      190689750
Email:   cabr9750@mylaurier.ca
__updated__ = "2020-01-30"
-------------------------------------------------------
"""
from functions import stack_maze

maze = {'Start': ['A'], 'A':['B', 'C'], 'B':[], 'C':['D', 'E'],
            'D':[], 'E':['F', 'X'], 'F':['G', 'H'], 'G':[], 'H':[]}

path = stack_maze(maze)
print(path)

