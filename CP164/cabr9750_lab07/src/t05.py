"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Jacob Cabral
ID:      190689750
Email:   cabr9750@mylaurier.ca
__updated__ = "2020-03-02"
-------------------------------------------------------
"""
from List_linked import List

list = List()
list2 = List()

list.append(1)
list.append(3)
list.append(5)
list.append(7)
 
list2.append(1)
list2.append(3)
list2.append(5)
list2.append(7)
list2.append(6)

list.union(list,list2)

for value in list:
    print(value)