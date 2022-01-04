"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  your name
ID:      your id
Email:   your email
__updated__ = "2020-01-19"
-------------------------------------------------------
"""
from copy import deepcopy


class Stack:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty stack. Data is stored in a Python list.
        Use: stack = Stack()
        -------------------------------------------------------
        Returns:
            a new Stack object (Stack)
        -------------------------------------------------------
        """
        self._values = []

    def push(self, value):
            """
            -------------------------------------------------------
            Pushes a copy of value onto the top of the stack.
            Use: stack.push(value)
            -------------------------------------------------------
            Parameters:
                value - value to be added to stack (?)
            Returns:
                None
            -------------------------------------------------------
            """
            self._values.append(deepcopy(value))
            return

    def is_empty (self):
        if len(self._values) == 0:
            isEmpty = True
        else:
            isEmpty = False
        return isEmpty
    def pop (self):
        assert len(self._values) > 0, "Cannot pop an empty stack"
        
        value = self._values.pop()
        return value

    def peek(self):
        """
        -------------------------------------------------------
        Peeks at the top of the stack.
        Use: value = s.peek()
        -------------------------------------------------------
        Postconditions:
            returns
            value - a copy of the value at the top of the stack -
                the value is not removed from the stack (?)
        -------------------------------------------------------
        """
        assert len(self._values) > 0, "Cannot peek at an empty stack"

        value = deepcopy(self._values[-1])
        return value
    
    def __len__(self):
        return len( self._values )
    
    def __str__(self):
        val = str(self._values)
        return val
    
    def __iter__(self):
        """
        FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the stack
        from top to bottom.
        Use: for v in s:
        -------------------------------------------------------
        Returns:
            value - the next value in the stack (?)
        -------------------------------------------------------
        """
        for value in self._values[::-1]:
            yield value
    
    def split_alt(self):
        """
        -------------------------------------------------------
        Splits the source stack into separate target stacks with values
        alternating into the targets. At finish source stack is empty.
        Use: target1, target2 = source.split_alt()
        -------------------------------------------------------
        Returns:
            target1 - contains alternating values from source (Stack)
            target2 - contains other alternating values from source (Stack)
        -------------------------------------------------------
        """
        target1 = Stack()
        target2 = Stack()
        i = 0
        
        while len(self._values) > 0:
            c = self._values.pop()
            
            if (i % 2) == 0:
                target1._values.append(c)
                i+= 1
            else:
                target2._values.append(c)
                i+= 1
        
        
        return target1,target2
    def combine(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source stacks into the current target stack.
        When finished, the contents of source1 and source2 are interlaced
        into target and source1 and source2 are empty.
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an array-based stack (Stack)
            source2 - an array-based stack (Stack)
        Returns:
            None
        -------------------------------------------------------
        """
        stack_select = True
        a = len(source1)
        b = len(source2)
        
        while (len(self._values) != (a + b)):
            if stack_select == True:
                if len(source1) != 0:
                    c = source1._values.pop()
                    self._values.append(c)
                    stack_select = not stack_select
                else:
                    stack_select = not stack_select
            elif stack_select == False:
                if len(source2) != 0:
                    c = source2._values.pop()
                    self._values.append(c)
                    stack_select = not stack_select
                else:
                    stack_select = not stack_select