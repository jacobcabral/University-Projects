'''
Created on 2020 M01 7

@author: jacob
'''
VOWELS = ['a', 'e', 'i', 'o', 'u']
TAIL = 'ay'

def max_diff(a):
    """
    -------------------------------------------------------
    Returns maximum absolute difference between adjacent values in a list.
    Use: md = max_diff(a)
    -------------------------------------------------------
    Parameters:
        a - a list of values (list of int)
    Returns:
        md - the largest absolute difference between adjacent
            values in a (int)
    -------------------------------------------------------
    """
    largest = 0
    if a == []:
        largest = 0
    else:
        for i in range(len(a)-1):
            if abs(a[i+1]-a[i]) > largest:
                largest = abs(a[i+1]-a[i])
    return largest


def is_valid(name):
    """
    -------------------------------------------------------
    Determines if name is a valid Python variable name.
    Variables names must start with a letter or an underscore.
    The rest of the variable name may consist of letters, numbers
    and underscores.
    Use: valid = is_valid(name)
    -------------------------------------------------------
    Parameters:
        name - a string to test as a Python variable name (str)
    Returns:
        valid - True if name is a valid Python variable name,
            False otherwise (boolean)
    -------------------------------------------------------
    """
    valid = True
    if name[0].isalpha() or name[0] == "_":
        for i in range (1,len(name)):
            if name[i].isalpha() == False and name[i].isnumeric() == False and name[i] != "_":
                valid = False
                
    else:
        valid = False
    return valid
            
def matrix_flatten(a):
    """
    -------------------------------------------------------
    Flatten the contents of 2D list a. A 'flattened' list is a
    2D list that is converted into a 1D list.
    Use: b = matrix_flatten(a):
    -------------------------------------------------------
    Parameters:
        a - a 2D list (2D list of ?)
    Returns:
        b - the flattened version of a (list of ?)
    -------------------------------------------------------
    """
    b = []
    for i in range (len(a)):
        for j in range (len(a[i])):
            b.append(a[i][j])
    return b
        
def matrix_stats(a):
    """
    -------------------------------------------------------
    Determines the smallest, largest, total, and average of
    the values in the 2D list a.
    Use: small, large, total, average = matrix_stats(a):
    -------------------------------------------------------
    Parameters:
        a - a 2D list of numbers (2D list of float)
    Returns:
        small - the smallest number in a (float)
        large - the largest number in a (float)
        total - the total of all numbers in a (float)
        average - the average of all numbers in a (float)
    -------------------------------------------------------
    """
    b = []
    for i in range (len(a)):
        for j in range (len(a[i])):
            b.append(a[i][j])
    small = 0
    for x in range (len(b)):
        if b[x] < small:
            small = b[x]
    large = 0
    for x in range (len(b)):
        if b[x] > large:
            large = b[x]
    total = 0
    for z in range (len(b)):
        total += b[z]
    average = total / len(b)
    
    return small,large,total,average

def matrixes_add(a, b):
    """
    -------------------------------------------------------
    Sums the contents of matrixes a and b. a and b must have
    the same number of rows and columns.
    a and b must be unchanged.
    Use: c = matrixes_add(a, b)
    -------------------------------------------------------
    Parameters:
        a - a 2D list (2D list of int/float)
        b - a 2D list (2D list of int/float)
    Returns:
        c - the matrix sum of a and b (2D list of int/float)
    -------------------------------------------------------
    """
    assert len(a) == len(b) and len(a[0]) == len(b[0])
    row = []
    c = []
    for x in range (len(a)):
        row.append(0)
    for i in range (len(a[0])):
        c.append(row)
    for i in range(len(a)):    
        for j in range(len(b[0])): 
            c[i][j] = a[i][j] + b[i][j] 
    
    return c


def matrixes_multiply(a, b):
    """
    -------------------------------------------------------
    Multiplies the contents of matrixes a and b.
    If a is mxn in size, and b is nxp in size, then c is mxp.
    a and b must be unchanged.
    Use: c = matrixes_multiply(a, b)
    -------------------------------------------------------
    Parameters:
        a - a 2D list (2D list of int/float)
        b - a 2D list (2D list of int/float)
    Returns:
        c - the matrix multiple of a and b (2D list of int/float)
    -------------------------------------------------------
    """
    #len(a) x len(b[0)
    
    
    row = []
    c = []
    for x in range (len(b[0])):
        row.append(0)
    for i in range (len(a)):
        c.append(row)
    
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                c[i][j] += a[i][k] * b[k][j]
    return c

def matrix_rotate_right(a):
    """
    -------------------------------------------------------
    Returns a copy of a 2D matrix rotated to the right.
    Use: b = matrix_rotate_right(a)
    -------------------------------------------------------
    Parameters:
        a - a 2D list of values (2d list of int/float)
    Returns:
        b - the rotated 2D list of values (2D list of int/float)
    -------------------------------------------------------
    """
    b = []
    for i in range(len(a[0])):
        b.append([])
        for j in range(len(a)):
            b[i].append(a[len(a)-j-1][i])
    return b

def file_analyze(fv):
    """
    -------------------------------------------------------
    Analyzes the characters in a file.
    The contents of the file must be unchanged.
    Use: u, l, d, w, r = file_analyze(fv)
    -------------------------------------------------------
    Parameters:
        fv - an already open file reference (file variable)
    Returns:
        u - the number of uppercase letters in the file (int)
        l - the number of lowercase letters in the file (int)
        d - the number of digits in the file (int)
        w - the number of whitespace characters in the file (int)
        r - the number of remaining characters in the file (int)
    -------------------------------------------------------
    """
    u,l,d,w,r = 0
    
    text = fv.readlines
    text = [line.rstrip('\n') for line in open(fv.name)]
    for line in fv:
        for x in line:
            if x.isupper():
                u += 1
            elif x.isnumeric():
                d += 1
            elif x.islower():
                l += 1
            elif x.isspace():
                w += 1
    
    r = len(text) - u - l - d - w
    return u,l,d,w,r           
def dsmvwl(s):
    """
    -------------------------------------------------------
    Disemvowels a string. out contains all the characters in s
    that are not vowels. ('y' is not considered a vowel.) Case is preserved.
    Use: out = dsmvl(s)
    -------------------------------------------------------
    Parameters:
       s - a string (str)
    Returns:
       out - s with the vowels removed (str)
    -------------------------------------------------------
    """
    vowels = ["a", "e", "i", "o", "u"]
    for x in vowels:
        s = s.replace(x, '')
    return s

def pig_latin(word):
    """
    -------------------------------------------------------
    Converts a word to Pig Latin. The conversion is:
    - if a word begins with a vowel, add "way" to the end of the word.
    - if the word begins with consonants, move all consonants to the
    end of the word and add "ay" to the end of that.
    "y" is treated as a consonant if it is the first character in the word,
    and as a vowel for anywhere else in the word.
    Preserve the case of the word - i.e. if the first character of word
    is upper-case, then the new first character should also be upper case.
    Use: pl = pig_latin(word)
    -------------------------------------------------------
    Parameters:
        word - a string to convert to Pig Latin (str)
    Returns:
        pl - the Pig Latin version of word (str)
    ------------------------------------------------------
    """
    pyg = 'ay'

    if len(word) > 0 and word.isalpha():
        word = word.lower()
        first = word[0]
        if first == ('a' or 'e' or 'i' or 'o' or 'u'):
            new_word = word + pyg
        
        else:
            new_word = word[1:] + first + pyg
            pl = new_word
    if word[0].isupper():
        pl =  pl[0].upper()
        
    
    return pl
    
    