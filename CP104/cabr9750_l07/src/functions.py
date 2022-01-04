"""
------------------------------------------------------------------------
[functions for lab 7]
------------------------------------------------------------------------
Author: Jacob Cabral
ID:     190689750
Email:  cabr9750@mylaurier.ca
__updated__ = "2019-05-10"
------------------------------------------------------------------------
"""
from random import randint

def hi_lo_game(high):
    """
    -------------------------------------------------------
    Plays a random higher-lower guessing game.
    Use: count = hi_lo_game(high)
    -------------------------------------------------------
    Parameters:
        high - maximum random value (int > 1)
    Returns:
        count - the number of guesses the user made (int)
    -------------------------------------------------------
    """
    
    number = randint(1, high)
    
    guess = 0
    count = 0
    
    while guess != number:
        guess = int(input("Guess: "))
        
        if guess < number:
            print("Too low, try again.")
            count += 1
        elif guess > number:
            print("Too high, try again.")
            count += 1
        else:
            print("Congratulations - good guess!")
            count +=1
            return count
        
        
def population_growth(target, current, rate):
    """
    -------------------------------------------------------
    Determines the number of years to reach a target population.
    Use: years = population_growth(target, current, rate)
    -------------------------------------------------------
    Parameters:
        target - target population (int > current)
        current - current population (int > 1)
        rate - percent rate of growth (float > 0)
    Returns:
        years - the number of years to reach target population (int)
    -------------------------------------------------------
    """
    rate = rate/100
    years = 0
    while target > current:
        current = current * (1 + rate)
        years += 1
    return years

def positive_statistics():
    """
    -------------------------------------------------------
    Asks a user to enter a series of positive numbers, then calculates
    and returns the minimum, maximum, total, and average of those numbers.
    Stop processing values when the user enters a negative number.
    The first number entered must be positive.
    Use: minimum, maximum, total, average = positive_statistics()
    -------------------------------------------------------
    Returns:
        minimum - smallest of the entered values (float)
        maximum - largest of the entered values (float)
        total - total of the entered values (float)
        average - average of the entered values (float)
    ------------------------------------------------------
    """
    count = 1
    minimum = 0
    maximum = 0
    average = 0
    total = 0
    entry = float(input("First positive value: "))
    if entry > 0:
        minimum = entry
        maximum = entry
        average = entry
        total = entry
        
        entry = float(input("Next positive value: "))
        
        while entry >= 0:
            count += 1       
            if entry > maximum:
                maximum = entry
                
            if entry < minimum:
                minimum = entry
          
            total = total + entry
            average = ((total)/count)    
        
            
            entry = float(input("Next positive value: "))
    return minimum,maximum,total,average
        
def get_int(low, high):
    """
    -------------------------------------------------------
    Asks a user for an integer value between low and high, and
    continues asking until an acceptable value is input.
    Use: value = get_int(low, high)
    -------------------------------------------------------
    Parameters:
        low - the lowest acceptable integer (inclusive) (int)
        high - the higest acceptable integer (inclusive) (int > low)
    Returns:
        value - a number between low and high (int)
    ------------------------------------------------------
    """
    value = "err"
    
    while True:
        value = int(input("Enter a value between {:.0f} and high {:.0f} ".format(low, high)))
        
        if value > high:
            print("Value entered is too high")
        elif value < low:
            print("Value entered is too low")
        else:
            print()
            break
    
    return value

def meal_costs():
    """
    -------------------------------------------------------
    Asks a user the costs of breakfast, lunch, and supper for each
    day the user was away. Assumes there is at least one day, and
    after entering data for each day asks the user whether they want
    to enter data for another day. Calculates total costs for meals.
    Use: b_total, l_total, s_total, a_total = meal_costs()
    -------------------------------------------------------
    Returns:
        b_total - total breakfasts cost (float)
        l_total - total lunches cost (float)
        s_total - total suppers cost (float)
        a_total - all meals cost (float)
    ------------------------------------------------------
    """
    cont = "Y"
    b_total = 0
    l_total = 0 
    s_total = 0
    day = 1
    a_total = 0
    while cont == "Y":
        print("for day {:.0f}".format(day))
        day = day + 1
        print()
        breakfast = float(input("How much was breakfast? $"))
        b_total = b_total + breakfast
        lunch = float(input("How much was lunch? $"))
        l_total = l_total + lunch
        supper = float(input("How much was supper? $"))
        s_total = s_total + supper
        total = breakfast + lunch + supper
        a_total = a_total + total
        print("Your total for the day was ${:.2f}".format(total))
        cont = str(input("Were you away another day (Y/N)? ")) 
        print()
    return b_total, l_total, s_total, a_total
    
            