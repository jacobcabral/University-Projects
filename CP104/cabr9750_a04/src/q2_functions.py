"""
------------------------------------------------------------------------
[the functions for q2]
------------------------------------------------------------------------
Author: Jacob Cabral
ID:     190689750
Email:  cabr9750@mylaurier.ca
__updated__ = "2019-10-01"
------------------------------------------------------------------------
"""
import random
def math_quiz ():
    '''
    ------------------------------------------------------------------------------
    Generates two integers between 0 and 999, and presents them as an addition problem to the user
    ------------------------------------------------------------------------------
    Use: math_quiz():
    ------------------------------------------------------------------------------
    Paramaters - none
    Returns - none
    ------------------------------------------------------------------------------
    '''
    first_number = random.randint(0,1000)
    second_number = random.randint(0,1000)
    total_random = first_number + second_number
    
    print(" ",first_number)
    print("+",second_number)
    
    user_entry = int(input("Answer: "))
    
    if user_entry == total_random:
        print("Congratulations, correct answer!")
    else: 
        print("Incorrect - the answer should be: {:.0f}".format(total_random))    
        