"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Jacob Cabral
ID:     190689750
Email:  cabr9750@mylaurier.ca
__updated__ = "2019-05-10"
------------------------------------------------------------------------
"""
from functions import generate_matrix_num

rows = int(input("Enter rows: "))
cols = int(input("Enter cols: "))
low = int(input("Enter low val: "))
high = int(input("Enter high val: "))
value_type = str(input("Enter value type: "))

matrix = generate_matrix_num(rows, cols, low, high, value_type)
print(matrix)