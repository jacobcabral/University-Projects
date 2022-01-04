"""
-------------------------------------------------------
[testing matrixes_multiply]
-------------------------------------------------------
Author:  Jacob Cabral
ID:      190689750
Email:   cabr9750@mylaurier.ca
__updated__ = "2020-01-14"
-------------------------------------------------------
"""
from functions import matrixes_multiply

a = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

b = [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]

c = matrixes_multiply(a, b)

print(c)
