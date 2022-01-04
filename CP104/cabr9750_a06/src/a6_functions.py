"""
------------------------------------------------------------------------
[functions for assignment 6]
------------------------------------------------------------------------
Author: Jacob Cabral
ID:     190689750
Email:  cabr9750@mylaurier.ca
__updated__ = "2019-10-22"
------------------------------------------------------------------------
"""
import math
INVESTMENT_GROWTH = 0.05

def calc_profit (principal,year):
    '''
    -------------------------------------------------------
    Description: calculates the profit of a house after a certain amount of years at a rate of 5% a year
    Use: calc_profit(principal, year)
    -------------------------------------------------------
    Parameters:
        principal - the inital investment on the home (int>0)
    Returns:
         none
    ------------------------------------------------------

    '''

    print()
    print("Year Value (Million Dollars) ")
    print("---- -----------------------")
    
    principal = principal/1000000
    yearcount = 1
    for x in range (year):
        principal = principal + (INVESTMENT_GROWTH * principal)
        #principal = round(principal, 6)
        print("   {:.0f}                {:.6f}".format(yearcount,principal))
        yearcount += 1
    
    

def perfect_square (num):
    '''
    -------------------------------------------------------
    Description - prints all the perfect squares under the chosen number
    Use: perfect_square(num)
    -------------------------------------------------------
    Parameters:
        num - the number you are trying to find all perfect squares under (int > 1)
    Returns:
         none
    ------------------------------------------------------

    '''

    if num < 0:
        print("\nYou did not enter a positive integer")
    else:
        perfect_squares = []
        for x in range (1,num):
            if math.sqrt(x) % 1 == 0:
                perfect_squares.append(x)
                
        
        print('\nPerfect Squares below {:d} are:'.format(num), end = ' ')
        print(*perfect_squares, sep = ', ') 
        
def factorial (num):
    '''
    -------------------------------------------------------
    Description - calculates the factorial of a given positive integer
    Use: result = factorial(num)
    -------------------------------------------------------
    Parameters:
        num - the integer being entered (int)
    Returns:
         result - the factorial of "num" (int>0)
    ------------------------------------------------------

    '''

    if num < 0:
        result = -1
        
    else:
        result = 1
        for x in range (num,1,-1):
            result = result * x
            
    return result

def is_prime (num):
    '''
    -------------------------------------------------------
    Description - checks and sees if the given number is a prime number
    Use: result = is_prime(num)
    -------------------------------------------------------
    Parameters:
        num - the number that is being checked to see if it is prime (int)
    Returns:
         result - weather the number is prime or not (boolean)
    ------------------------------------------------------

    '''

    for i in range(2, num//2):
        if (num % i) == 0:
            result = False
            break
    else:
        result = True
    return result
        

        
    

    
            
            
        
