"""
------------------------------------------------------------------------
[functions for lab 5]
------------------------------------------------------------------------
Author: Jacob Cabral
ID:     190689750
Email:  cabr9750@mylaurier.ca
__updated__ = "2019-10-09"
------------------------------------------------------------------------
"""


def magic_date(day, month, year):
    """
    -------------------------------------------------------
    Determines if a date is magic. A date is magic if the day
    times the month equals the year.
    Use: magic = magic_date(day, month, year)
    -------------------------------------------------------
    Parameters:
        day - numeric day (int > 0)
        month - numeric month (int > 0)
        year - numeric two-digit year (int > 0)
    Returns:
        magic - True if date is magic, False otherwise (boolean)
    -------------------------------------------------------
    """
    
    if ((day * month) == year):
        result = True
    else: 
        result = False
        
    return result

def is_leap(year):
    """
    -------------------------------------------------------
    Determines if a year is a leap year. Every year that is
    exactly divisible by four is a leap year, except for years
    that are exactly divisible by 100, but these centurial years
    are leap years if they are exactly divisible by 400. For
    example, the years 1700, 1800, and 1900 are not leap years,
    but the years 1600 and 2000 are.
    Use: result = is_leap(year)
    -------------------------------------------------------
    Parameters:
        year - a year (int > 0)
    Returns:
        result - True if year is a leap year,
            False otherwise (boolean)
    ------------------------------------------------------
    """
    if (year % 400 == 0):
        result = True
    elif (year % 100 == 0):
        result = False
    elif (year % 4 == 0):
        result = True
    else:
        result = False
    return result

def roman_numeral(n):
    """
    -------------------------------------------------------
    Convert 1-10 to Roman numerals.
    Use: numeral = roman_numeral(n)
    -------------------------------------------------------
    Parameters:
        n - number to convert to Roman numerals (int)
    Returns:
        numeral - Roman numeral version of n, None if n is not
          between 1 and 10 inclusive. (str)
    -------------------------------------------------------
    """
    if (n == 1):
        numeral = "I"
    elif (n ==2):
        numeral = "II"
    elif (n ==3):
        numeral = "III"
    elif (n ==4):
        numeral = "IV"
    elif (n ==5):
        numeral = "V"
    elif (n ==6):
        numeral = "VI"
    elif (n ==7):
        numeral = "VII"
    elif (n ==8):
        numeral = "VIII"
    elif (n ==9):
        numeral = "IX"
    elif (n ==10):
        numeral = "X"
    else:
        numeral = None   
        
    return numeral

def pay_raise(status, years, salary):
    
    RAISE_AT_10F = 0.05
    RAISE_AT_04F = 0.015
    RAISE_AT_10P = 0.03
    RAISE_AT_4P = 0.01
    RAISE_AT_OTHER = 0.02
    
    """
    -------------------------------------------------------
    Calculates pay raises for employees. Pay raises are based on:
    status: Full Time ('F)' or Part Time ('P')
    and years of service
    Raises are:
        5% for full time >= 10 years service
        1.5% for full time < 4 years service
        3% for part time > 10 years service
        1% for part time < 4 years service
        2% for all others
    Use: new_salary = pay_raise(status, years, salary)
    -------------------------------------------------------
    Parameters:
        status - employment type (str - 'F' or 'P')
        years - number of years employed (int > 0)
        salary - current salary (float > 0)
    Returns:
        new_salary - employee's new salary (float).
    -------------------------------------------------------
    """
   
    
    if (status == "F"):
        if(years >= 10):
            new_salary = salary * (RAISE_AT_10F + 1)
        elif(years < 4):
            new_salary = salary * (RAISE_AT_04F + 1)
        else:
            new_salary = salary * (RAISE_AT_OTHER + 1)
    elif (status == "P"):
        if (years > 10):
            new_salary = salary * (RAISE_AT_10P + 1)
        elif (years < 4):
            new_salary = salary * (RAISE_AT_4P + 1)
        else:
            new_salary = salary * (RAISE_AT_OTHER + 1)
    else:
        new_salary = "The status entered is not valid"
    
    return new_salary

def fast_food():
    
    BURGER_PRICE = 6.00
    WINGS_PRICE = 8.00
    FRIES_PRICE = 1.50
    SALAD_PRICE = 2.00
    """
    -------------------------------------------------------
    Food order function.
    Prices:
        Burger: $6.00
        Wings: $8.00
        Fries combo: add $1.50
        Salad combo: add $2.00
    Use: price = fast_food()
    -------------------------------------------------------
    Returns:
        price - the price of one meal (float)
    -------------------------------------------------------
    """
   
    
    inital_order = str(input("Order B - burger or W - wings: "))
    combo_selection = str(input("Make it a combo? (Y/N): "))
    if (inital_order == "B"):
        if(combo_selection == "Y"):
            combo_food = str(input("Add F - fries or S - salad: "))
            if(combo_food == "F"):
                price = BURGER_PRICE + FRIES_PRICE
            else:
                price = BURGER_PRICE + SALAD_PRICE
        if(combo_selection == "N"):
            price = BURGER_PRICE
    elif (inital_order == "W"):
        if(combo_selection == "Y"):
            combo_food = str(input("Add F - fries or S - salad: "))
            if(combo_food == "F"):
                price = WINGS_PRICE + FRIES_PRICE
            else:
                price = WINGS_PRICE + SALAD_PRICE
        if(combo_selection == "N"):
            price = WINGS_PRICE
    else:
        price = "Invalid type"
        
    return price
            
            
                
                
    
    
        
          
    
        