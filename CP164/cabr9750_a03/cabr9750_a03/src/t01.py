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
from functions import stack_split_alt
from Stack_array import Stack

source = [5,7,8,9,12,14,8]
s = Stack()
for i in range (len(source)):
    s.push(source[i])
target1, target2 = stack_split_alt(s)

print(target1)
print(target2)