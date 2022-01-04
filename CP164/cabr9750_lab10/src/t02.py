"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Jacob Cabral
ID:      190689750
Email:   cabr9750@mylaurier.ca
__updated__ = "2020-03-11"
-------------------------------------------------------
"""
from Sorts_List_linked import Sorts
from test_Sorts_List_linked import test_sort
print("n:   100       |      Comparisons       | |         Swaps          |")
print("Algorithm      In Order Reversed   Random In Order Reversed   Random")
print("-------------- -------- -------- -------- -------- -------- --------")

test_sort("Insertion Sort",Sorts.insertion_sort)
test_sort("Selection Sort",Sorts.selection_sort)
test_sort("Bubble Sort",Sorts.bubble_sort)
test_sort("Merge Sort",Sorts.merge_sort)
test_sort("Quick Sort",Sorts.quick_sort)
test_sort("Comb Sort",Sorts.comb_sort)
