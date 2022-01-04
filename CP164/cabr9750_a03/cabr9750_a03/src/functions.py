"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Jacob Cabral
ID:      190689750
Email:   cabr9750@mylaurier.ca
__updated__ = "2020-01-28"
-------------------------------------------------------
"""

from Stack_array import Stack

def stack_split_alt(source):
    """
    -------------------------------------------------------
    Splits the source stack into separate target stacks.
    When finished source stack is empty. Values are
    pushed alternately onto the returned target stacks.
    Use: target1, target2 = stack_split_alt(source)
    -------------------------------------------------------
    Parameters:
        source - the stack to split into two parts (Stack)
    Returns:
        target1 - contains alternating values from source (Stack)
        target2 - contains other alternating values from source (Stack)
    -------------------------------------------------------
    """
    stack_select = True
    target1 = Stack()
    target2 = Stack()
    
    while len(source) != 0:
        c = source.pop()
        if stack_select == True:
            target1.push(c)
            stack_select = not stack_select
            
        elif stack_select == False:
            target2.push(c)
            stack_select = not stack_select
            
            
    return target1,target2



def stack_combine(source1, source2):
    """
    -------------------------------------------------------
    Combines two source stacks into a target stack.
    When finished, the contents of source1 and source2 are interlaced
    into target and source1 and source2 are empty.
    Use: target = stack_combine(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - a stack (Stack)
        source2 - another stack (Stack)
    Returns:
        target - the contents of the source1 and source2
            are interlaced into target (Stack)
    -------------------------------------------------------
    """
    target = Stack()
    stack_select = True
    a = len(source1)
    b = len(source2)
    
    while (len(target) != (a + b)):
        
        if stack_select == True:
            
            if len(source1) != 0:
                c = source1.pop()
                
                target.push(c)
                stack_select = not stack_select
            else:
                stack_select = not stack_select
                
        elif stack_select == False:
            
            if len(source2) != 0:
                c = source2.pop()
                target.push(c)
                
                stack_select = not stack_select
            else:
                stack_select = not stack_select
                
    return target
def is_palindrome_stack(string):
    """
    -------------------------------------------------------
    Determines if string is a palindrome. Ignores case, digits, spaces, and
    punctuation in string.
    Use: palindrome = is_palindrome_stack(string)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        palindrome - True if string is a palindrome, False otherwise (bool)
    -------------------------------------------------------
    """
    s = Stack()
    string = string.lower()
    string = string.strip()
    palindrome = True
    compare = ""
    for i in range (len(string)):
        if string[i].isalpha():
            compare = compare + string[i]
            s.push(string[i])
    
    reconstructed_string = ""
    while len(s) > 0:
        c = s.pop()
        reconstructed_string = reconstructed_string + c
        
    if reconstructed_string == compare:
        palindrome = True
    else:
        palindrome = False
    return palindrome

def postfix(string):
    """
    -------------------------------------------------------
    Evaluates a postfix expression.
    Use: answer = postfix(string)
    -------------------------------------------------------
    Parameters:
        string - the postfix string to evaluate (str)
    Returns:
        answer - the result of evaluating string (float)
    -------------------------------------------------------
    """
    s = Stack()
    x = string.split()
    for i in range (len(x)):
        if x[i].isnumeric():
            c = int(x[i])
            s.push(c)
        elif x[i] == "+" or "*" or "/" or "-":
            a = s.pop()
            b = s.pop()
            if x[i] == "+":
                val = b + a
            elif x[i] == "-":
                val = b-a
            elif x[i] == "/":
                val = b/a
            elif x[i] == "*":
                val = a*b
            s.push(val)
            
    answer = s.pop()
    return answer           
            
def stack_maze(maze):
    """
    -------------------------------------------------------
    Solves a maze using Depth-First search.
    Use: path = stack_maze(maze)
    -------------------------------------------------------
    Parameters:
        maze - dictionary of points in a maze, where each point
            represents a corridor end or a branch. Dictionary
            keys are the name of the point followed by a list of
            branches, if any. First point is named 'Start', exit
            is named 'X' (dict)
    Returns:
        path - list of points visited before the exit is reached,
            None if there is no exit (list of str)
    -------------------------------------------------------
    """
    path = []
    key = 'Start'
    value = maze[key]
    key = value[0]
    stack = Stack()
    stack.push(key)
    path.append(key)
    
    
    
    while(key != 'X' and path != None):
        value = maze[key]
        while(len(value) != 0 and stack.peek() != 'X'):
            stack.push(value.pop(0))
            
        if(not stack.is_empty()):    
            key = stack.pop()
            path.append(key)
        else:
            path = None
        
    

    return path  
    
    
    
    
        
        
            
    

