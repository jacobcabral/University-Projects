"""
------------------------------------------------------------------------
[functions for t2]
------------------------------------------------------------------------
Author: Jacob Cabral
ID:     190689750
Email:  cabr9750@mylaurier.ca
__updated__ = "2019-10-09"
------------------------------------------------------------------------
"""

def pocket_color (num):
    '''
    -------------------------------------------------------
    Description - Returns the color of the pocket on a roulette wheel defined by a user entered integer
    Use: color = pocket_color (num)
    -------------------------------------------------------
    Parameters:
        num - the number entered by the user that should correspond to a pocket on the roulette wheel (int => 0)
    Returns:
         color - the color of the pocket that corresponds to the number, or an error message if a non corresponding integer is entered (string)
    ------------------------------------------------------

    '''
    if (num == 0):
        color = "green"
    elif (1 <= num <=10):
        if(num % 2 == 0):
            color = "black"
        else:
            color = "red"
    elif (11 <= num <=18):
        if (num % 2 == 0):
            color = "red"
        else:
            color = "black"
    elif (19 <= num <=28):
        if (num % 2 == 0):
            color = "black"
        else:
            color = "red"
    elif (29 <= num <=36):
        if (num % 2 == 0):
            color = "red"
        else:
            color = "black"
    else:
        color = "ERROR"
            
    return color
            
    
            