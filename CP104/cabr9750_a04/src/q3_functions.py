"""
------------------------------------------------------------------------
[the functions for q3]
------------------------------------------------------------------------
Author: Jacob Cabral
ID:     190689750
Email:  cabr9750@mylaurier.ca
__updated__ = "2019-05-10-02"
------------------------------------------------------------------------
"""
def num_day (day_int):
    '''
    ------------------------------------------------------------------------------
    takes the user entered variable and shows the day of the week it corrosponds to
    ------------------------------------------------------------------------------
    Use: num_day (day_int)
    ------------------------------------------------------------------------------
    Paramaters
        num_day - the day of the week in numerical form entered by the user (int > 0)
    returns
        a print statement telling the user their number either corrosponds to a day, or is not valid
    ------------------------------------------------------------------------------
    '''
    if day_int == 1:
        print("The number 1 corresponds to Monday")
    elif day_int == 2:
        print("The number 2 corresponds to Tuesday")    
    elif day_int == 3:
        print("The number 3 corresponds to Wednesday")    
    elif day_int == 4:
        print("The number 4 corresponds to Thursday")
    elif day_int == 5:
        print("The number 5 corresponds to Friday")
    elif day_int == 6:
        print("The number 6 corresponds to Saturday")      
    elif day_int == 7:
        print("The number 7 corresponds to Sunday")  
    else:
        print("Sorry, that is not a valid number")            