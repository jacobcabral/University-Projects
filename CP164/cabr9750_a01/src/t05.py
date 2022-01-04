"""
-------------------------------------------------------
[testing matrixes_add]
-------------------------------------------------------
Author:  Jacob Cabral
ID:      190689750
Email:   cabr9750@mylaurier.ca
__updated__ = "2020-01-14"
-------------------------------------------------------
"""
from functions import matrixes_add

a = [[1,2,3], 
    [4 ,5,6], 
    [7 ,8,9]] 

b = [[9,8,7], 
    [6,5,4], 
    [3,2,1]] 

c = matrixes_add(a, b)
print(c)
