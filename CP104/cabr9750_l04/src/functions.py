"""
------------------------------------------------------------------------
[the functions for lab 4]
------------------------------------------------------------------------
Author: Jacob Cabral
ID:     190689750
Email:  cabr9750@mylaurier.ca
__updated__ = "2019-10-02"
------------------------------------------------------------------------
"""
import math
SECONDS_IN_DAY = 86400
SECONDS_IN_HOUR = 3600
SECONDS_IN_MINUTE = 60

VALUE_OF_LOONIE = 1
VALUE_OF_TOONIE = 2
VALUE_OF_NICKEL = 0.05
VALUE_OF_DIME = 0.1
VALUE_OF_QUARTER = 0.25

def diameter(radius):
    """
    -------------------------------------------------------
    Calculates and returns diameter of a circle.
    Use: d = diameter(radius)
    -------------------------------------------------------
    Parameters:
        radius - radius of a circle (float >= 0)
    Returns:
        d - diameter of a circle (float)
    ------------------------------------------------------
    """
    final_diameter = radius * 2
    return final_diameter

def square_pyramid(base, height):
    """
    -------------------------------------------------------
    Calculates and returns the slant height, area, and
    volume of a square pyramid given the base and perpendicular
    height.
    Use: sh, a, v = square_pyramid(base, height)
    -------------------------------------------------------
    Parameters:
        base - length of the base of the pyramid (float > 0)
        height - perpendicular height of the pyramid (float > 0)
    Returns:
        sh - slant height of the square pyramid (float)
        a - area of the square pyramid (float)
        v - volume of the square pyramid (float)
    ------------------------------------------------------
    """
    sh = math.sqrt(((base/2)**2) + (height**2))
    
    a = (base**2) + 2 * base * math.sqrt(((base/2)**2) + (height**2))
    
    v = ((base**2) * (height/3))
    
    return sh,a,v

def total_change(nickels, dimes, quarters, loonies, toonies):
    """
    -------------------------------------------------------
    Calculates the total value of a set of coins in dollars.
    Each coin is worth:
        nickel:  $0.05
        dime:    $0.10
        quarter: $0.25
        loonie:  $1.00
        toonie:  $2.00
    Use: total = total_change(nickels, dimes, quarters,
        loonies, toonies)
    -------------------------------------------------------
    Parameters:
        nickels - number of nickels (int >= 0)
        dimes - number of dimes (int >= 0)
        quarters - number of quarters (int >= 0)
        loonies - number of loonies (int >= 0)
        toonies - number of toonies (int >= 0)
    Returns:
        total - total value of coins (float)
    -------------------------------------------------------
    """
    
    
    total =VALUE_OF_NICKEL * nickels + VALUE_OF_DIME * dimes + VALUE_OF_QUARTER * quarters + VALUE_OF_LOONIE * loonies + VALUE_OF_TOONIE * toonies
    
    return total
   
def time_split(initial_seconds):
    """
    -------------------------------------------------------
    Converts total seconds into days, hours, minutes, and seconds.
    Use: days, hours, minutes, seconds = time_split(initial_seconds)
    -------------------------------------------------------
    Parameters:
        initial_seconds - time elapsed (int >= 0)
    Returns:
        days - number of days in initial_seconds (int)
        hours - remaining hours in initial_seconds (int)
        minutes - remaining minutes in initial_seconds (int)
        seconds - remaining seconds in initial_seconds (int)
    -------------------------------------------------------
    """
  
    days = initial_seconds//SECONDS_IN_DAY
    hours = (initial_seconds%SECONDS_IN_DAY)//SECONDS_IN_HOUR
    minutes = (initial_seconds%SECONDS_IN_HOUR)//SECONDS_IN_MINUTE
    seconds = ((initial_seconds%SECONDS_IN_HOUR)%SECONDS_IN_MINUTE)
    
    
    return days,hours,minutes,seconds
    
    
    

def computer_costs(computer_cost, computers_bought, commission_percent):
    """
    -------------------------------------------------------
    Calculates purchase costs of computers
    Use: pre_commission_cost, total_cost = computer_costs(computer_cost,
        computers_bought, commission_percent)
    -------------------------------------------------------
    Parameters:
        computer_cost - per unit cost (float >= 0)
        computers_bought - units bought (int >= 0)
        commission_percent - wholesaler commission (float >= 0)
    Returns:
        pre_commission_cost - cost before commission (float)
        total_cost - cost after commission (float)
    -------------------------------------------------------
    """
    pre_commission_cost =computer_cost * computers_bought
    total_cost = ((commission_percent/100) * pre_commission_cost) + pre_commission_cost
    
    return pre_commission_cost,total_cost




