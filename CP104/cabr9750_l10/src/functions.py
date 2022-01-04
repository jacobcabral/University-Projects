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
#1,3,8,9,14
def customer_record(fv, n):
    """
    -------------------------------------------------------
    Find the n-th record in a comma-delimited sequential file.
    Records are numbered starting with 0.
    Use: record = customer_record(fv, n)
    -------------------------------------------------------
    Parameters:
        fv - file to search (file - open for reading)
        n - the number of the record to return (int > 0)
    Returns:
        record - a list of the fields of the n-th record if it exists,
            an empty list otherwise (list)
    -------------------------------------------------------
    """
    input = fv.readline()
    result = []
    i = 0
    while (input != "" and result == []):
        if i == n:
            result = (input.strip().split(","))
        
        input = fv.readline()
        i += 1
    return result


def customer_best(fv):
    """
    -------------------------------------------------------
    Find the customer with the largest balance.
    Assumes file is not empty.
    Use: result = customer_best(fv)
    -------------------------------------------------------
    Parameters:
        fv - file to search (file - open for reading)
    Returns:
        result - the record with the greatest balance (list)
    -------------------------------------------------------
    """
    line = fv.readline()
    result = []
    balance_check = -1
    
    while(line != ""):
        record = line.strip().split(',')
        bal = float(record[3])
        
        if(bal > balance_check):
            balance_check = float(bal)
            result = record
            
        line = fv.readline()
    
    return result

def append_increment(fv):
    """
    -------------------------------------------------------
    Appends a number to the end of the fv. The number appended
    is the last number in the file plus 1.
    Assumes file is not empty.
    Use: num = append_increment(fv)
    -------------------------------------------------------
    Parameters:
        fv - file to search (file - open for reading/writing)
    Returns:
        num - the number appended to the file (int)
    ------------------------------------------------------
    """
    line = fv.readline()
    while(line != ""):
        last = line
        line = fv.readline()
    
    last = int(last) + 1
    fv.write('\n'+ str(last))
    return last

def count_frequency_value(fv, value):
    """
    -------------------------------------------------------
    Counts the number of appearances of value in fv.
    Use: count = count_frequency_value(fv, value)
    -------------------------------------------------------
    Parameters:
        fv - file to search (file - open for reading)
        value - the value to count (int)
    Returns:
        count - the number of appearance of value in fv (int)
    ------------------------------------------------------
    """
    i = 0
    for x in fv:
        a = int(x)
        if(a == value):
            i += 1
            
        else:
            continue
        
    return i

def file_copy_n(fv_1, fv_2, n):
    """
    -------------------------------------------------------
    Copies n record from fv_1 (starting from the beginning of the file) to fv2
    Use: file_copy_n(fv_1, fv_2, n)
    -------------------------------------------------------
    Parameters:
        fv_1 - file to search (file - open for reading)
        fv_2 - file to search (file - open for appending)
    Returns:
        None
    ------------------------------------------------------
    """
    for i in range(0, n):
        fv_2.write(fv_1.readline())

    return None


    