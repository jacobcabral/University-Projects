"""
-------------------------------------------------------
Tests various linked sorting functions.
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
Section: CP164 C
__updated__ = "2019-04-27"
-------------------------------------------------------
"""
# Imports
import random

from List_linked import List
from Number import Number
from Sorts_List_linked import Sorts

# Constants
SIZE = 100  # Size of array to sort.
XRANGE = 1000  # Range of values in random arrays to sort.
TESTS = 100  # Number of random arrays to generate.

SORTS = (
    ('Bubble Sort', Sorts.bubble_sort),
    ('Insertion Sort', Sorts.insertion_sort),
    ('Merge Sort', Sorts.merge_sort),
    ('Quick Sort', Sorts.quick_sort),
    ('Selection Sort', Sorts.selection_sort),
)


def create_sorted():
    """
    -------------------------------------------------------
    Creates a sorted List of Number objects.
    Use: values = create_sorted()
    -------------------------------------------------------
    Returns:
        values - a sorted list of SIZE Number objects (List of Number)
    -------------------------------------------------------
    """
    values = List()
    size = SIZE-1
    while size >= 0:
        values.insert(0,Number(size))
        size -= 1
    return values


def create_reversed():
    """
    -------------------------------------------------------
    Create a reversed List of Number objects.
    Use: values = create_reversed()
    -------------------------------------------------------
    Returns:
        values - a reversed list of SIZE Number objects (List of Number)
    -------------------------------------------------------
    """
    values = List()
    for i in range (SIZE):
        values.insert(0,Number(i))
    
    return values


def create_randoms():
    """
    -------------------------------------------------------
    Create a 2D list of Number objects.
    Use: lists = create_randoms()
    -------------------------------------------------------
    Returns:
        lists - TEST lists of SIZE Number objects containing
            values between 0 and XRANGE (list of List of Number)
    -------------------------------------------------------
    """
    lists = List()
    for i in range(TESTS):
        new = []
        for j in range(SIZE):
            new.append(Number(random.randint(0,XRANGE)))
        lists.insert(0,new)   
    return lists


def test_sort(title, func):
    """
    -------------------------------------------------------
    Tests a sort function with Number data and prints the number 
    of comparisons necessary to sort an array:
    in order, in reverse order, and a list of Lists in random order.
    Use: test_sort(title, func)
    -------------------------------------------------------
    Parameters:
        title - name of the sorting function to call (str)
        func - the actual sorting function to call (function)
    Returns:
        None
    -------------------------------------------------------
    """
    a = create_sorted()
    b = create_reversed()
    c = create_randoms()
    func(a)
    comp_a = a[0].comparisons
    swap_a = Sorts.swaps
    Number.comparisons = 0
    func(b)
    swap_b = Sorts.swaps
    comp_b = b[0].comparisons
    Number.comparisons = 0
    func(c)
    swap_c = Sorts.swaps
    comp_c = c[0][0].comparisons
    Number.comparisons = 0
    print("{:<15} {:>7} {:>8} {:>8} {:>8.2f} {:>8.2f} {:>8.2f}".format(title,comp_a,comp_b,comp_c,swap_a,swap_b,swap_c))
    print()
    return