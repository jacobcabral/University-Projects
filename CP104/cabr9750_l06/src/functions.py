"""
------------------------------------------------------------------------
[functions for lab 06]
------------------------------------------------------------------------
Author: Jacob Cabral
ID:     190689750
Email:  cabr9750@mylaurier.ca
__updated__ = "2019-10-23"
------------------------------------------------------------------------
"""

def sum_even(num):
    """
    -------------------------------------------------------
    Sums and returns the total of all even numbers from 2 to num (inclusive).
    Use: total = sum_even(num)
    -------------------------------------------------------
    Parameters:
        num - an integer (int > 0)
    Returns:
        total - sum of all even numbers from 2 to num (int)
    ------------------------------------------------------
    """
    total = 0
    for x in range (2,num + 1,2):   
        total = total + x
            
            
        
    return total


def draw_triangle(height, char):
    """
    -------------------------------------------------------
    Prints a triangle of height characters using
    the char character.
    Use: draw_triangle(height, char)
    -------------------------------------------------------
    Parameters:
        height - number of characters high (int > 0)
        char - the character to draw with (str, len() == 1)
    Returns:
        None
    ------------------------------------------------------
    """
   
    for i in range (1, height + 1):
        print("{}{}".format(" " * (height - i), char * (i * 2 - 1)))       
        
    
    return
    
    
    
    
    
def lumber(b_min, b_max, b_inc, h_min, h_max, h_inc):
    """
    -------------------------------------------------------
    Create a table of the engineering properties of lumber.
    Given the base and height of a piece of lumber in inches,
    different properties of a piece of lumber are calculated as:
        cross-sectional area = base × height
        moment of inertia = base × height^3 / 12
        section modulus = base × height^2 / 6
    Use: lumber(b_min, b_max, b_inc, h_min, h_max, h_inc)
    -------------------------------------------------------
    Parameters:
        b_min - minimum value of base (int > 0)
        b_max - maximum value of base (int > b_min)
        b_inc - increment in base value (int > 0)
        h_min - minimum value of height (int > 0)
        h_max - maximum value of height (int > h_min)
        h_inc - increment in height value (int > 0)
    Returns:
        None
    ------------------------------------------------------
    """
        
    print("              Cross-Sectional  Moment of  Section")
    print("Base  Height  Area             Inertia    Modulus")
    print("\n")
    for x in range (b_min, b_max + 1,b_inc):
        for y in range (h_min,h_max + 1,h_inc):
            cross_sectional = x * y
            moment_of_intertia = (x * (y**3)/12)
            section_modulus = (x * (y**2)/6)
            print("{:3.0f}{:9.0f}{:14.2f}{:13.2f}{:11.2f}".format(x,y,cross_sectional,moment_of_intertia,section_modulus))
    return
            
            
    
def treadmill(burnt_per_minute, start, end, inc):
        """
        -------------------------------------------------------
        Calculates and prints calories burnt on a treadmill over
        a given time range.
        Use: treadmill(burnt_per_minute, start, end, inc)
        -------------------------------------------------------
        Parameters:
            burnt_per_minute - calories burnt per minute (float > 0)
            start - start time in minutes (int > 0)
            end - end time in minutes (int >= start)
            inc - increment in minutes (int > 0)
        Returns:
            None
        ------------------------------------------------------
        """
    
        for i in range(start, end + inc, inc):
            print("Calories burned after {:d} minutes: {:.1f}".format(i, i * burnt_per_minute))
        return
            
            
            
def retirement(age, salary, increase):
        """
        -------------------------------------------------------
        Calculates a prints a table of how much a worker earns
        between age and retirement at 65.
        Use: retirement(age, salary, increase)
        -------------------------------------------------------
        Parameters:
            age - worker's current age (int > 0)
            salary - worker's current salary (float > 0)
            increase - percent increase in salary per year (float >= 0)
        Returns:
            None
        ------------------------------------------------------
        """
        
        print("""Age         Salary
    ------------------""")
        
        for i in range(age, age + 5):
            print("{:<2d}{:>16,.2f}".format(i, salary * (1 + (increase / 100)) ** (i - age)))
        print("...")
        print("{:<2d}{:>16,.2f}".format(65, salary * (1 + (increase / 100)) ** (65 - age)))
        return
