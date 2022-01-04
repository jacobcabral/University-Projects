"""
------------------------------------------------------------------------
[extracts the digits from a two digit number and gets their sum]
------------------------------------------------------------------------
Author: Jacob Cabral
ID:     190689750
Email:  cabr9750@mylaurier.ca
__updated__ = "2019-05-10"
------------------------------------------------------------------------
"""
integer_input = int(input("Enter a positive two digit integer: "))
first_digit = integer_input%10
second_digit = (integer_input//10)%10
total_value = first_digit + second_digit
integer_input = str(integer_input)
print("The sum of the two digits in the integer ("+integer_input+") is:",total_value)