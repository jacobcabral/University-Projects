"""
-------------------------------------------------------
Assignment 4, Task 1
-------------------------------------------------------
Author:  Jacob Cabral
ID:      190689750
Email:   cabr9750@mylaurier.ca
__updated__ = "2020-02-01"
-------------------------------------------------------
"""
# Imports
from Queue_circular import Queue

print("Creating the queue")
target = Queue(5)

print("Empty? {}".format(target.is_empty()))
print("Full? {}".format(target.is_full()))
print("Length: {}".format(len(target)))

print()
print("Adding:")
i = 0
while target.is_full() != True:
    i += 1
    target.insert(i)

print("Length: {}".format(len(target)))
print("Empty? {}".format(target.is_empty()))
print("Full? {}".format(target.is_full()))

print()
print("Queue:")
for v in target:
    print(v)
    
print()
print("Removing:")
target.remove()
print("Length: {}".format(len(target)))
print("Empty? {}".format(target.is_empty()))
print("Full? {}".format(target.is_full()))
print()
print("Queue:")
for v in target:
    print(v)
    
print()
print("Peek: {}".format(target.peek()))