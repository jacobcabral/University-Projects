"""
-------------------------------------------------------
Assignment 4, Task 3
-------------------------------------------------------
Author:  Jacob Cabral
ID:      190689750
Email:   cabr9750@mylaurier.ca
__updated__ = "2020-02-01"
-------------------------------------------------------
"""
# Imports
from Priority_Queue_array import Priority_Queue

#creating the priority queue
source = Priority_Queue()

#input
amount = int(input("How many values in the queue? "))
print()
for i in range(amount):
    source.insert(int(input("Enter your value to insert into the queue: ")))

print()
print("Queue:")  
for value in source:
    print(value)

print()
key = int(input("Enter your key: "))

#calling the functions
target1, target2 = source.split_key(key)

print()
#output
print("Target1:")
for value in target1:
    print(value)
print()
print("Target2:")
for value in target2:
    print(value)