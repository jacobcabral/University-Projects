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
from Stack_array import Stack


source = [5,7,8,9,12,14,8]
s = Stack()
for i in range (len(source)):
    s.push(source[i])
    
target1, target2 = s.split_alt()
print(target1)
print(target2)

