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