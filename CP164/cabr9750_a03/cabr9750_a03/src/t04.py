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

source1 = [8, 12, 8, 5]
source2 = [14, 9, 7]
one = Stack()
two = Stack()
for i in range (len(source1)):
    one.push(source1[i])

for j in range (len(source2)):
    two.push(source2[j])
    
target = Stack()
target.combine(one, two)
print(target)

