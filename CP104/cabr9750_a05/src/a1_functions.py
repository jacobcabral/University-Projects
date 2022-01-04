"""
------------------------------------------------------------------------
[functions for q1]
------------------------------------------------------------------------
Author: Jacob Cabral
ID:     190689750
Email:  cabr9750@mylaurier.ca
__updated__ = "2019-10-08"
------------------------------------------------------------------------
"""
def max_three(x,y,z):
    '''
    -------------------------------------------------------
    Description - finds the average of the smallest two integers from a given set of 3
    Use: average = max_three(x, y, z)
    -------------------------------------------------------
    Parameters:
        x, y, z - the three integers passed to the program (float)
    Returns:
         average - the average of the two smallest integers (float)
    ------------------------------------------------------

    '''
    if (x >= y) and (x >= z):
        average = (y + z)/2
    elif (y >= x) and (y >= z):
        average = (x + z)/2
    elif (z >= x and z >= y):
        average = (x + y)
        
    return average
  
    