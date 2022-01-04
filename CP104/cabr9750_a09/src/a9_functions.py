"""
------------------------------------------------------------------------
[functions for a9]
------------------------------------------------------------------------
Author: Jacob Cabral
ID:     190689750
Email:  cabr9750@mylaurier.ca
__updated__ = "2019-11-23"
------------------------------------------------------------------------
"""
import statistics
import os


def sum_numbers (myfile):
    '''
    -------------------------------------------------------
    Description: reads through a file and gets the sum of all the numbers in the file that are seperated by shitespace
    Use: numbers, total = sum_numbers(myfile)
    -------------------------------------------------------
    Parameters:
        myfile - a file handle that conatins a string with numbers (file)
    Returns:
         numbers - a list containing all the numbers extracted form the string (list)
         total - the total value of all extracted digits (int)
    ------------------------------------------------------

    '''
    #create a list to hold the numbers from the string and the total
    numbersfromstring = []
    sumnumbers = 0
    #open and read the file and split it by whitespace
    
    contents = myfile.read()
    myfile.close()
    text = contents.split()
    #loop through the array and test if a number is whole, numeric and positive, then add it to the list if it is
    for i in range (len(text)):
        if text[i].isdigit():
            numbersfromstring.append(text[i])
        
    numbersfromstring = list(map(int,numbersfromstring))
    help = numbersfromstring[:]
    for item in numbersfromstring: 
        if item < 0: 
            help.remove(item) 

    sumnumbers = sum(help)
    
    return help, sumnumbers


def find_median (myfile):
    '''
    -------------------------------------------------------
    Description finds the median in a given file of integers
    Use: 
    -------------------------------------------------------
    Parameters:
        myfile - a file handle that conatins numbers (file)
    Returns:
         sortedints - a list of the sortedints numbers found in the file (list of ints)
         median - the median of the list (int)
    ------------------------------------------------------

    '''
    sortedints = []
    
    if os.stat("numbers.txt").st_size == 0:
        sortedints = []
        median = None
    numbers = myfile.readlines()
    
    for x in range (len(numbers)):
        numbers[x] = numbers[x].split()
        
    
    for i in range (len(numbers)):
        for j in range (len(numbers[0])):
            sortedints.append(int(numbers[i][j]))
        
    median = statistics.median(sortedints)
    sortedints = sortedints.sort()
    
    return sortedints,median

def analysis_file (file_in):
    '''
    -------------------------------------------------------
    Description - checks a string and counts the lowercase, uppercase, digits, and whitespace in the file
    Use - uppercase,lowercase,digits,whitespace = analysis_file(file_in)
    -------------------------------------------------------
    Parameters:
        file_in - the file handle of the file to be counted (file)
    Returns:
         uppercase - the number of uppercase characters in the file (int)
         lowercase - the number of lowercase characters in the file (int)
         digits - the number of numeric characters in the file (int)
         whitespace - the number of whitespace characters in the file (int)
    ------------------------------------------------------

    '''
    
    lowercase = 0
    uppercase = 0
    whitespace = 0
    digits = 0
    
    text = file_in.readlines
    text = [line.rstrip('\n') for line in open("text.txt")]
    for line in file_in:
        for x in line:
            if x.isupper():
                uppercase += 1
            elif x.isnumeric():
                digits += 1
            elif x.islower():
                lowercase += 1
            elif x.isspace():
                whitespace += 1
            
    return uppercase,lowercase,digits,whitespace
def valid_sn (txt_srl):
    '''
    -------------------------------------------------------
    Description - Checks the serial number and returns true or false depending on if it is valid or not 
    Use: result = valid_sn(txt_srl)
    -------------------------------------------------------
    Parameters:
        txt_srl - text string of the serial number (txt_srl)
    Returns:
         result - if the serial number is true or falsee(boolean)
    ------------------------------------------------------

    '''


    if txt_srl[0:3] == "SN/":
        if txt_srl[3:7].isnumeric():
            if txt_srl[7] == "-":
                if txt_srl[8:12].isnumeric():
                    valid = True
                else:
                    valid = False
            else:
                valid = False
        else:
            valid = False
    else:
        valid = False
        
            
    return valid

def valid_sn_file(serial_number,serial_valid,serial_invalid):
    '''
    -------------------------------------------------------
    Description - validates a text file full of serial numbers
    Use: serial_number,serial_valid,serial_invalid = valid_sn_file(serial_number,serial_valid,serial_invalid)
    -------------------------------------------------------
    Parameters:
        serial_unumber - text file of serial numbers
        serial_valid - the file of valid serial numbers
        serial_invalid - the file of invalid serial numbers
    Returns:
         none
    ------------------------------------------------------

    '''
    serial_numbers = serial_number.readline()
    while (serial_numbers != ""):
        serial_numbers = serial_numbers.rstrip("\n")
        result = valid_sn(serial_numbers)
        if result == True:
            serial_valid.write(serial_numbers+"\n")
        else:
            serial_invalid.write(serial_numbers+"\n")
    
    
        serial_numbers = serial_number.readline()
    
    
    
            
            