"""
------------------------------------------------------------------------
[functions for a8]
------------------------------------------------------------------------
Author: Jacob Cabral
ID:     190689750
Email:  cabr9750@mylaurier.ca
__updated__ = "2019-05-10"
------------------------------------------------------------------------
"""


def sum_digit_string (my_str):
    '''
    -------------------------------------------------------
    Description
    calculates the value of all the integers in a string
    Use: total = sum_digit_string(my_str)
    -------------------------------------------------------
    Parameters:
        my_str - the string containing integers being counted (str)
    Returns:
         total - the total  value of the integers in the string (int>0)
    ------------------------------------------------------

    '''
    valuehold = 0
    valuelist = []
    valid = ['1','2','3','4','5','6','7','8','9','0']
    for i in range (len(my_str)):
        if my_str[i] in valid:
            valuehold = int(my_str[i])
            valuelist.append(valuehold)
    return sum(valuelist)

def find_frequent (my_str):
    '''
    -------------------------------------------------------
    Description: Parses the string and returns the most used character
    Use: frequent = find_frequent(my_str)
    -------------------------------------------------------
    Parameters:
        my_str - the string containing characters being counted (str)
    Returns:
         frequent- a list of the most frequent characters in the string (list)
    ------------------------------------------------------

    '''
    checked = [" ", ]
    frequent = []
    most_frequent = 0
    for i in range (len(my_str)):
        if (my_str[i] not in checked):
            checked.append(my_str[i])
            
            if my_str.count(my_str[i]) > most_frequent:
                most_frequent = my_str.count(my_str[i])
                frequent = []
                frequent.append(my_str[i])
            elif my_str.count(my_str[i]) == most_frequent:
                frequent.append(my_str[i])

    if my_str == "":
        frequent = None
    return frequent

def string_capitalizer (my_str):
    '''
    -------------------------------------------------------
    Description: Parses the string and capitalizes the sentence
    Use: new_string = string_capitalizer(my_str)
    -------------------------------------------------------
    Parameters:
        my_str - the string containing sentence being capitalized(str)
    Returns:
         newString - the string with the sentence capitalized (str)
    ------------------------------------------------------

    '''
    
    cap = True
    newString = ''
    
    if my_str == "":
        my_str == None
    for letter in my_str:
        if letter == "?" or letter == ".":
            cap = True
            newString+= letter
        elif cap == True and letter.isalpha():
            cap = False
            newString += letter.upper()
        else:
            newString+= letter
    return newString

def is_word_chain (my_list):
    '''
    -------------------------------------------------------
    Description:checks a list of words to ensure it's a word chain
    Use: chain_result = is_word_chain(my_list)
    -------------------------------------------------------
    Parameters:
        my_list - list of words to be checked for a word chain (list of str)
    Returns:
         chain_result - the result of the list being checked as a word chain (boolean)
    ------------------------------------------------------

    '''
    chain_result = True
    if len(my_list) > 1 or my_list == []:
        for i in range(len(my_list)):
            if i+1 != len(my_list):
                str1 = my_list[i]
                str2 = my_list[i+1]
                if str1[-1] != str2[0]:
                    chain_result = False
    else:
                    chain_result = False
    return chain_result
            
        
    
                
    
                
            
        
            
            
        