"""
------------------------------------------------------------------------
[functions for q3]
------------------------------------------------------------------------
Author: Jacob Cabral
ID:     190689750
Email:  cabr9750@mylaurier.ca
__updated__ = "2019-05-10"
------------------------------------------------------------------------
"""

def base_price (call_length):
    PRICE_PER_MINUTE = 0.08
    '''
    -------------------------------------------------------
    Description - calculates the base price of the call based on the given number of minutes the call lasts
    Use: base_price = base_price (call_length)
    -------------------------------------------------------
    Parameters:
        call_length - the amount of time the call lasts in minutes (int >=0)
    Returns:
        base_price - the base price of the call in dollars (int > 0)
    ------------------------------------------------------

    '''
    
    base_price = PRICE_PER_MINUTE * call_length
    
    return base_price

def time_discount(base_price, call_hour):
    TIME_DISCOUNT_MIDNIGHT = 0.25
    TIME_DISCOUNT_MORNING = 0.5
    
    '''
    -------------------------------------------------------
    Description - takes the base price of the call and the hour the call was made at and attempts to apply any time discounts
    Use: price_time_discount = time_discount (call_price,call_hour)
    -------------------------------------------------------
    Parameters:
        base_price - the base price of the call obtained from base_price
    Returns:
         price_time_discount - the base price modified by subrtacting the time discount , if the call did not qualify for discounts none were applied (int > 0)
    ------------------------------------------------------

    '''
    
    if (18 <= call_hour <= 23):
        discount = base_price * TIME_DISCOUNT_MIDNIGHT
        price_time_discount = base_price - discount
    elif(0<= call_hour <= 8):
        discount = base_price * TIME_DISCOUNT_MORNING
        price_time_discount = base_price - discount
    else:
        price_time_discount = base_price
    
    return price_time_discount

def Length_discount (price_time_discount, call_length):
    
    '''
    -------------------------------------------------------
    Description - takes the time-discounted price of the call and the length of the call and attempts to apply any length discounts
    Use: price_length_discount = length_discount (price_time_discount, call_length)
    -------------------------------------------------------
    Parameters:
        price_time_discount - the time-discounted price of the call, made by subtracting a time discount from the base prife if applicable (int > 0)
    Returns:
         price_length_discount - the time discounted price modified by subrtacting the length discount , if the call did not qualify for discounts none were applied (int > 0)
    ------------------------------------------------------

    '''
    discount = 0
    LENGTH_DISCOUNT = 0.10
    if(call_length >= 30):
        discount = price_time_discount * LENGTH_DISCOUNT
        price_length_discount = price_time_discount - discount
    else:
        price_length_discount = price_time_discount
        
    return price_length_discount
        
        


        
        