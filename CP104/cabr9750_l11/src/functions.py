"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Jacob Cabral
ID:     190689750
Email:  cabr9750@mylaurier.ca
__updated__ = "2019-05-10"
------------------------------------------------------------------------
"""
from random import randint,uniform
def generate_matrix_num(rows, cols, low, high, value_type):
    """
    -------------------------------------------------------
    Generates a 2D list of numbers of the given type, 'float' or 'int'.
    (To generate random float number use random.uniform and to
    generate random integer number use random.randint)
    Use: matrix = generate_matrix_num(rows, cols, low, high, value_type)
    -------------------------------------------------------
    Parameters:
        rows - number of rows in the list (int > 0)
        cols - number of columns (int > 0)
        low - low value of range (float)
        high - high value of range (float > low)
        value_type - type of values in the list, 'float' or 'int' (str)
    Returns:
        matrix - a 2D list of random numbers (2D list of float/int)
    -------------------------------------------------------
    """
    
    matrix = []
    if value_type == "float":
        for i in range (rows):
            row = []
            for j in range (cols):
                row.append(uniform(low,high))
        
            matrix.append(row)
    else:
        for i in range (rows):
            row = []
            for j in range (cols):
                row.append(randint(low,high))
        
            matrix.append(row)
        
    return matrix

def print_matrix_num(matrix, value_type):
    """
    -------------------------------------------------------
    Prints the contents of a 2D list in a formatted table.
    Prints float values with 2 decimal points and prints row and
    column headings.
    Use: print_matrix_num(matrix, 'float')
    Use: print_matrix_num(matrix, 'int')
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of values (2D list)
        value_type - type of values in the list, 'float' or 'int' (str)
    Returns:
        None.
    -------------------------------------------------------
    """
    if(value_type == 'float'):
        print("      ", end='')
        for i in range(len(matrix[0])):
            print("{:5d}".format(i), end='')

        print()
        for y in range(len(matrix)):
            print(" {:5d}".format(y), end='')
            for x in matrix[y]:
                print("{:5.2f}".format(x), end='')
            print()
    
    else:
        print("      ", end='')
        for i in range(len(matrix[0])):
            print("{:5d}".format(i), end='')

        print()
        for y in range(len(matrix)):
            print(" {:5d}".format(y), end='')
            for x in matrix[y]:
                print("{:5d}".format(x), end='')
                
            print()
    return

def find_position(matrix):
    """
    -------------------------------------------------------
    Determines the first locations [row, column] of smallest and
    largest values in a 2D list.
    Use: s_loc, l_loc = find_position(matrix)
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of numbers (2D list)
    Returns:
        s_loc - a list of of the row and column location of
            the smallest value in matrix (list of int)
        l_loc - a list of of the row and column location of
            the largest value in matrix (list of int)
    -------------------------------------------------------
    """
    high = matrix[0][0] - 1
    low = matrix[0][0] + 1
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            
            if matrix[i][j] > high:
                high = matrix[i][j]
                l_loc = [i, j]
            
            if matrix[i][j] < low:
                low = matrix[i][j]
                s_loc = [i, j]
    
    return s_loc, l_loc

def scalar_multiply(matrix, num):
    """
    -------------------------------------------------------
    Update matrix by multiplying each element of matrix by num.
    Use: scalar_multiply(matrix, num)
    -------------------------------------------------------
    Parameters:
        matrix - the matrix to multiply (2D list of int/float)
        num - the number to multiply by (int/float)
    Returns:
        None
    ------------------------------------------------------
    """
    for i in range (len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] = (matrix[i][j]) * num
    return
    
def matrix_equal(matrix1, matrix2):  # 15
    """
    -------------------------------------------------------
    Compares two matrices to see if they are equal - i.e. have the
    same contents in the same locations.
    Use: equal = matrix_equal(matrix1, matrix2)
    -------------------------------------------------------
    Parameters:
        matrix1 - the first matrix (2D list of ?)
        matrix2 - the second matrix (2D list of ?)
    Returns:
        equal - True if matrix1 and matrix2 are equal,
            False otherwise (boolean)
    ------------------------------------------------------
    """
    equal = True
       
    if len(matrix1) == len(matrix2) and len(matrix1[0]) == len(matrix2[0]):
        for i in range(len(matrix1)):
            for j in range(len(matrix1[0])):
                if matrix1[i][j] != matrix2[i][j]:
                    equal = False
    else:
        equal = False
    return equal


