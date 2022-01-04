"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Jacob Cabral
ID:     190689750
Email:  cabr9750@mylaurier.ca
__updated__ = "2019-10-10"
------------------------------------------------------------------------
"""
def quadrant (x_coordinate,y_coordinate):
    '''
    -------------------------------------------------------
    Description - Finds the coordinate on the Cartesian plane defined by the point passed to the program
    Use: quadrant_value = quadrant (x_coordinate, y_coordinate)
    -------------------------------------------------------
    Parameters:
        x_coordinate - the x value of the set of coordinates (int)
        y_coordinate - the y value of the set of coordinates (int)
    Returns:
         quadrant_value - the shortened version of the number of the quadrant that the point lies in (String)
    ------------------------------------------------------

    '''
    if (x_coordinate > 0):
        if (y_coordinate > 0):
            quadrant_value = "Q1"
        else:
            quadrant_value = "Q4"
    elif (x_coordinate < 0):
        if (y_coordinate > 0):
            quadrant_value = "Q2"
        else:
            quadrant_value = "Q3"
    
    elif (x_coordinate == 0 and y_coordinate == 0):
        quadrant_value = "Q1"
        
    elif(x_coordinate == 0):
        if (y_coordinate > 0):
            quadrant_value = "Q1"
        else:
            quadrant_value = "Q3"
        
    
    return quadrant_value
        