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
def is_hydroxide(chemical): #q1
    """
    -------------------------------------------------------
    Determines if a chemical formula is a hydroxide.
    Use: hydroxide_state = is_hydroxide(chemical)
    -------------------------------------------------------
    Parameters:
    chemical - a chemical formula (str)
    Returns:
    hydroxide - True if chemical is a hydroxide(ends in 'OH'),
    False otherwise (boolean)
    -------------------------------------------------------
    """
    hydroxide_state = False
    
    if chemical[-2:] == "OH":
        hydroxide_state = True

    return hydroxide_state

def validate_code(product_code): #q4
    """
    -------------------------------------------------------
    Parses a given product code and prints whether the various parts are valid.
    A product code has three parts:
        The first three letters describe the product category and must
        all be in upper case.
        The next four digits are the product ID.
        The remaining characters describe the product's qualifiers,
        such as colour, size, etc. and always begins with an uppercase letter.
    Use: validate_code(product_code)
    -------------------------------------------------------
    Parameters:
        product_code - a product code (str)
    Returns:
        None
    -------------------------------------------------------
    """
    idnum = product_code[3:7]
    if product_code[:3].isupper() == True and len(product_code[:3]) == 3:
        print("Category",product_code[:3], "is valid.")
    else:
        print("Category",product_code[:3], "is not valid.")
       
    if idnum.isdigit() == True and len(idnum) == 4:
        print("ID", idnum,"is valid.") 
    else:
        print("ID", idnum,"is not valid.") 
    
    if len(product_code)-1 >= 7:
        if product_code[7].isupper() == True:
            print("Qualifier" , product_code[7:],"is valid." )
        else:
            print("Qualifier" , product_code[7:],"is not valid." )
    else:
            print("Qualifier" , product_code[7:],"is not valid." )
    return

def password_strength(password): #q5
    """
    -------------------------------------------------------
    Checks the strength of a given password. A password is
    strong if it contains at least eight characters, has a
    combination of upper-case and lower-case letters, and
    includes digits. Prints one or more of:
    not long enough - if password less than 8 characters
    no digits - if password has no digits
    no upper case - if password has no upper case letters
    no lower case - if password has no lower case letters
    Use: password_strength(password)
    -------------------------------------------------------
    Parameters:
    password - the password to be checked (str)
    Returns:
    None
    ------------------------------------------------------
    """
    num = 0
    lower = 0
    upper = 0 
    length = len(password)
    
    for x in range (0, len(password)):
        
        if password[x].isdigit():
            num = num + 1
        
        elif password[x].islower():
            lower += 1
        
        elif password[x].isupper():
            upper +=1
            
    if length < 8:
                print("not long enough") 
            
    if num == 0:
                print("no digits")
            
    if upper == 0:
                print("no upper case")
            
    if lower == 0:
                print("no lower case")

    return

def text_analyze(txt): # 10
    """
    -------------------------------------------------------
    Analyzes txt and returns the number of uppercase letters,
    lowercase letters, digits, and number of whitespaces in txt.
    Use: uppr, lowr, dgts, whtspc = text_analyze(txt)
    -------------------------------------------------------
    Parameters:
    txt - the text to be analyzed (str)
    Returns:
    uppr - number of uppercase letters in txt (int >= 0)
    lowr - number of lowercase letters in txt (int >= 0)
    dgts - number of digits in txt (int >= 0)
    whtspc - number of white spaces in the text (spaces, tabs, linefeeds) (int >= 0)
    ------------------------------------------------------
    """
    
    uppr = 0
    lowr = 0
    dgts = 0
    whtspc = 0
    
    for i in txt:
        if i.isupper():
            uppr += 1
        elif i.islower():
            lowr += 1
        elif i.isdigit():
            dgts += 1
        elif i == " ":
            whtspc += 1
    
    return uppr, lowr, dgts, whtspc

def calculate(expr): # 15
    """
    -----------------------------------------------------------------
    Treats expr as a math expression and evaluates it.
    expr must have the following format:
    operand1 operator operand2
    operators are: +, -, *, /, %
    operands are one-digit integer numbers
    Return None if second operand is zero for division.
    Use: result = calculate(expr)
    -----------------------------------------------------------------
    Parameters:
    expr - an arithmetic expression to be calculated (str)
    Returns:
    result - The result of arithmetic expression (float)
    -----------------------------------------------------------------
    """
    
    equation = expr.split(' ')
    
    if equation[1] == "+":
        result = int(equation[0]) + int(equation[2])
    elif equation[1] == "-":
        result = int(equation[0]) - int(equation[2])
    elif equation[1] == "*":
        result = int(equation[0]) * int(equation[2])
    elif equation[1] == "/":
        if equation[2] == "0":
            result = None
        else:
            result = int(equation[0]) / int(equation[2])
    elif equation[1] == "%":
        if equation[2] == "0":
            result = None
        else:
            result = int(equation[0]) % int(equation[2])
    
    return result
        
            
            
    
                    
        
        