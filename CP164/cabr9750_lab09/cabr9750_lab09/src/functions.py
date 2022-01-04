"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Jacob Cabral
ID:      190689750
Email:   cabr9750@mylaurier.ca
__updated__ = "2020-03-21"
-------------------------------------------------------
"""
def hash_table(val,list):
    """
    -------------------------------------------------------
    Print a hash table of a set of values. The format is:
    Hash     Slot Key
    -------- ---- --------------------
    1652346    3 Dark City, 1998
    848448    6 Zulu, 1964
    Do not create an actual Hash_Set.
    Use: something = hash_table(val,list)
    -------------------------------------------------------
    Parameters:
       slots - the number of slots available (int > 0)
       values - the values to hash (list of ?)
    Returns:
       None
    -------------------------------------------------------
    """
    print("Hashes")
    print("Hash      Slot Key")
    print("======    ==== ====================")
    '''
    for i in foods:
        value = Food.__hash__(i)
        print("  {:4}       {} {},{}".format(value,value%7,i.name,i.origin))
    
    
    '''
    for i in list:
        value = hash(i)
        print('{:8d} {:4d} {:s}, {:d}'.format(value,value%7,i.title,i.year))

    return