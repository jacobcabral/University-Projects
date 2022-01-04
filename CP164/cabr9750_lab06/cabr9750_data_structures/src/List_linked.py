"""
-------------------------------------------------------
Linked version of the list ADT.
-------------------------------------------------------
Author:  Jacob Cabral
ID:      190689750
Email:   cabr9750@mylaurier.ca
Term:    Winter 2020
__updated__ = "2020-01-16"
-------------------------------------------------------
"""
from copy import deepcopy

class _List_Node:

    def __init__(self, value, next_):
        """
        -------------------------------------------------------
        Initializes a list node that contains a copy of value
        and a link to the next node in the list.
        Use: node = _List_Node(value, _next)
        -------------------------------------------------------
        Parameters:
            _value - value value for node (?)
            _next - another list node (_List_Node)
        Returns:
            a new _List_Node object (_List_Node)
        -------------------------------------------------------
        """
        self._value = deepcopy(value)
        self._next = next_


class List:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty list.
        Use: lst = List()
        -------------------------------------------------------
        Returns:
            a new List object (List)
        -------------------------------------------------------
        """
        self._front = None
        self._rear = None
        self._count = 0


    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the list is empty.
        Use: b = lst.is_empty()
        -------------------------------------------------------
        Returns:
            True if the list is empty, False otherwise.
        -------------------------------------------------------
        """
        return self._count == 0

    
    def __len__(self):
        """
        -------------------------------------------------------
        Returns the number of values in the list.
        Use: n = len(lst)
        -------------------------------------------------------
        Returns:
            the number of values in the list.
        -------------------------------------------------------
        """
        return self._count


    def prepend(self, value):
        """
        -------------------------------------------------------
        Adds a copy of value to the front of the List.
        Use: lst.prepend(value)
        -------------------------------------------------------
        Parameters:
            value - a data element. (?)
        Returns:
            None
        -------------------------------------------------------
        """
        if(self._count > 0):
            self._front = _List_Node(value, self._front)
        
        else:
            self._front = self._rear = _List_Node(value, None)
        
        self._count += 1
        return 


    def append(self, value):
        """
        ---------------------------------------------------------
        Adds a copy of value to the end of the List.
        Use: lst.append(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        if(self._count > 0):
            pointer = self._front
            while(pointer._next is not None):
                pointer = pointer._next
                
            pointer._next = self._rear = _List_Node(value, None)
        
        else:
            self._rear = self._front = _List_Node(value, None)
        
        self._count += 1
        return 


    def insert(self, i, value):
        """
        -------------------------------------------------------
        A copy of value is added to index i, following values are pushed right.
        If i outside of range of -len(list) to len(list) - 1, the value is 
        prepended or appended as appropriate.
        Use: lst.insert(i, value)
        -------------------------------------------------------
        Parameters:
            i - index value (int)
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        if(i <= -self._count or i == 0):
            self.prepend(value)
            
        elif(i >= self._count):
            self.append(value)

        else:
            if(i < 0):
                i = self._count - abs(i)
            
            j = 0
            perv = None
            curr = self._front
            while(j < i):
                perv = curr
                curr = curr._next
                j += 1
                
            new_node = _List_Node(value, curr)
            perv._next = new_node
            self._count += 1
        
        return


    def _linear_search(self, key):
        """
        -------------------------------------------------------
        Searches for the first occurrence of key in list.
        Private helper method.
        (iterative algorithm)
        Use: previous, current, index = self._linear_search(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            previous - pointer to the node previous to the node containing key (_ListNode)
            current - pointer to the node containing key (_ListNode)
            index - index of the node containing key (int)
        -------------------------------------------------------
        """ 
        i = 0
        found = False
        previous = None
        current = self._front
        if(self._count > 0):
            if(self._count == 1 and current._value == key):
                found = True
            
            else:
                while(i < self._count and not found):
                    if(current._value == key):
                        found = True
                    
                    else:   
                        previous = current
                        current = current._next
                        i+= 1

        return (previous, current, i) if found else (previous, None, -1)


    def remove(self, key):
        
        """
        -------------------------------------------------------
        Finds, removes, and returns the first value in list that matches key.
        Use: value = lst.remove(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            value - the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """
        i = self._linear_search(key)[2]
        if(i == -1):
            result = None

        else:
            result = self.pop(i)

        return result
    
    
    def remove1(self, key): 
        """
        -------------------------------------------------------
        Finds, removes, and returns the first value in list that matches key.
        Use: value = lst.remove(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            value - the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """
        p, n, i = self._linear_search(key)
        if(i == -1):
            result = None
            
        else:
            result = deepcopy(n._value)
            if(i == 0):
                self._front = self._front._next
                pointer = self._front
                if(pointer is not None):
                    while(pointer._next is not None):
                        pointer = pointer._next
                
                self._rear = pointer
                
            elif(i == self._count - 1):
                previous = None
                pointer = self._front
                while(pointer._next is not None):
                    previous = pointer
                    pointer = pointer._next
                
                previous._next = None
                self._rear = previous  
                
            else:
                p._next = n._next

            self._count -= 1
        
        return result
    

    def remove_front(self):
        """
        -------------------------------------------------------
        Removes the first node in the list and returns its value.
        Use: value = lst.remove_front()
        -------------------------------------------------------
        Returns:
            value - the first value in the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot remove from an empty list"
        value = deepcopy(self._front._value)
        if(self._front._next is not None):
            self._front = self._front._next

        else:
            self._front = self._rear = None
        
        self._count -= 1
        self._set_rear()
        return value 


    def remove_many(self, key):
        """
        -------------------------------------------------------
        Finds and removes all values in the list that match key.
        Use: lst.remove_many(key)
        -------------------------------------------------------
        Parameters:
            key - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        _, _, i= self._linear_search(key)
        while(i != -1):
            self.pop(i)
            _, _, i= self._linear_search(key)
        
        return


    def find(self, key):
        """
        -------------------------------------------------------
        Finds and returns a copy of the first value in list that matches key.
        Use: value = lst.find(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            value - a copy of the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """
        result = self._linear_search(key)[1]
        return None if result == None else deepcopy(result._value)


    def peek(self):
        """
        -------------------------------------------------------
        Returns a copy of the first value in list.
        Use: value = lst.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the first value in the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot peek at an empty list"
        return deepcopy( self._front._value )


    def index(self, key):
        """
        -------------------------------------------------------
        Finds location of a value by key in list.
        Use: n = lst.index(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            i - the index of the location of key in the list, -1 if
                key is not in the list.
        -------------------------------------------------------
        """
        return self._linear_search(key)[2]


    def _is_valid_index(self, i):
        """
        -------------------------------------------------------
        Private helper method to validate an index value.
        Python index values can be positive or negative and range from
          -len(list) to len(list) - 1
        Use: assert self._is_valid_index(i)
        -------------------------------------------------------
        Parameters:
            i - an index value (int)
        Returns:
            True if i is a valid index, False otherwise.
        -------------------------------------------------------
        """
        return -self._count <= i < self._count
    

    def __getitem__(self, i):
        """
        ---------------------------------------------------------
        Returns a copy of the nth element of the list.
        Use: value = l[i]
        -------------------------------------------------------
        Parameters:
            i - index of the element to access (int)
        Returns:
            value - the i-th element of list (?)
        -------------------------------------------------------
        """
        assert self._is_valid_index(i), "Invalid index value"
        
        j = 0
        pointer = self._front
        if(i < 0):
            i = self._count - abs(i)
        
        while(j < i):
            pointer = pointer._next
            j += 1
            
        return deepcopy(pointer._value)
    

    def __setitem__(self, i, value):
        """
        ---------------------------------------------------------
        Places a copy of value into the list at position n.
        Use: l[i] = value
        -------------------------------------------------------
        Parameters:
            i - index of the element to access (int)
            value - a data value (?)
        Returns:
            The i-th element of list contains a copy of value. The 
                existing value at i is overwritten.
        -------------------------------------------------------
        """
        assert self._is_valid_index(i), "Invalid index value"
        if(i < 0):
            i = self._count - abs(i)
            
        j = 0
        current = self._front
        while(j < i):
            current = current._next
            j += 1
        
        current._value = value
        return deepcopy(value) 


    def __contains__(self, key):
        """
        ---------------------------------------------------------
        Determines if the list contains key.
        Use: b = key in l
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            True if the list contains key, False otherwise.
        -------------------------------------------------------
        """
        return self._linear_search(key)[2] != -1


    def max(self):
        """
        -------------------------------------------------------
        Finds the maximum value in list.
        Use: value = lst.max()
        -------------------------------------------------------
        Returns:
            max_data - a copy of the maximum value in the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot find maximum of an empty list"
        pointer = self._front
        maximum = pointer._value
        while(pointer._next is not None):
            pointer = pointer._next
            if(pointer._value > maximum):
                maximum = deepcopy(pointer._value)
        
            else:
                continue
        
        return deepcopy(maximum)


    def min(self):
        """
        -------------------------------------------------------
        Finds the minimum value in list.
        Use: value = lst.min()
        -------------------------------------------------------
        Returns:
            min_data - a copy of the minimum value in the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot find maximum of an empty list"
        pointer = self._front
        minimum = pointer._value
        while(pointer._next is not None):
            pointer = pointer._next
            if(pointer._value < minimum):
                minimum = pointer._value
        
            else:
                continue
        
        return deepcopy(minimum)


    def count(self, key):
        """
        -------------------------------------------------------
        Finds the number of times key appears in list.
        Use: n = lst.count(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            number - number of times key appears in list (int)
        -------------------------------------------------------
        """
        pointer = self._front
        result = 0
        while(pointer is not None):
            if(pointer._value == key):
                result += 1
                
            pointer = pointer._next

        return result 


    def reverse(self):
        """
        -------------------------------------------------------
        Reverses the order of the elements in list.
        (iterative algorithm)
        Use: lst.reverse()
        -------------------------------------------------------
        Returns:
            The contents of list are reversed in order with respect
            to their order before the method was called.
        -------------------------------------------------------
        """
        prev = None
        curr = self._front
        while(curr is not None): 
            node = curr._next
            curr._next = prev 
            prev = curr
            curr = node
        
        self._front = prev 
        self._set_rear()
        return    


    def reverse_r(self):
        """
        -------------------------------------------------------
        Reverses the order of the elements in list.
        (recursive algorithm)
        Use: lst.reverse_r()
        -------------------------------------------------------
        Returns:
            The contents of list are reversed in order with respect
            to their order before the method was called.
        -------------------------------------------------------
        """
        self._reverse_r_aux(None, self._front)
        return
    
    
    def _reverse_r_aux(self, prev, curr):
        if(curr is not None):
            node = curr._next
            curr._next = prev 
            prev = curr
            curr = node
            self._reverse_r_aux(prev, node)
            
        else:
            self._front = prev 
            self._set_rear()
   
        return
            

    def clean(self):
        """
        ---------------------------------------------------------
        Removes duplicates from the list. The list contains 
        one and only one of each value formerly present in the list. 
        The first occurrence of each value is preserved.
        Use: source.clean()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """
        temp = List()
        node = self._front
        while(node is not None):
            if(node._value not in temp):
                temp.append(node._value)
                
            node = node._next
        
        self._front = temp._front
        self._count = temp._count
        self._set_rear()
        return
    

    def pop(self, *args):
        """
        -------------------------------------------------------
        Finds, removes, and returns the value in list whose index matches i.
        Use: value = lst.pop()
        Use: value = lst.pop(i)
        -------------------------------------------------------
        Parameters:
            args - an array of arguments (tuple of int)
            args[0], if it exists, is the index i
        Returns:
            value - if args exists, the value at position args[0], 
                otherwise the last value in the list, value is 
                removed from the list (?)
        -------------------------------------------------------
        """
        assert self._front is not None, "Cannot pop from an empty list"
        assert len(args) <= 1, "No more than 1 argument allowed"

        previous = None
        current = self._front

        if len(args) == 1:

            if args[0] < 0:
                # index is negative
                n = self._count + args[0]
            else:
                n = args[0]
            j = 0

            while j < n:
                previous = current
                current = current._next
                j += 1
        else:
            # find and pop the last element
            j = 0

            while j < (self._count - 1):
                previous = current
                current = current._next
                j += 1

        value = current._value
        self._count -= 1

        if previous is None:
            # Remove the first node.
            self._front = self._front._next

            if self._front is None:
                # List is empty, update _rear.
                self._rear = None
        else:
            # Remove any other node.
            previous._next = current._next

            if previous._next is None:
                # Last node was removed, update _rear.
                self._rear = previous
        return value

    
    def _swap(self, pln, prn):
        """
        -------------------------------------------------------
        Swaps the position of two nodes. The nodes in pln.next and prn.next 
        have been swapped, and all links to them updated.
        Use: self._swap(pln, prn)
        -------------------------------------------------------
        Parameters:
            pln - node before list node to swap (_List_Node)
            prn - node before list node to swap (_List_Node)
        Returns:
            None
        -------------------------------------------------------
        """
        if(pln == prn):
            return 
        
        a = None
        if(pln is not None):
            a = pln._next
            
        print(a._value)
            
        if(a is not None):
            pln._next = prn._next
            prn._next = a
        
        self._set_rear()
        return


    def is_identical(self, other):
        """
        ---------------------------------------------------------
        Determines whether two lists are identical. 
        (iterative version)
        Use: b = lst.is_identical(other)
        -------------------------------------------------------
        Parameters:
            other - another list (List)
        Returns:
            identical - True if this list contains the same values as
                other in the same order, otherwise False.
        -------------------------------------------------------
        """
        identical = self._count == other._count
        curr1 = self._front
        curr2 = other._front
        while(identical and curr1 is not None):
            identical = curr1._value == curr2._value
            curr1 = curr1._next
            curr2 = curr2._next

        return identical


    def is_identical_r(self, other):
        """
        ---------------------------------------------------------
        Determines whether two lists are identical. 
        (recursive version)
        Use: b = lst.identical_r(other)
        -------------------------------------------------------
        Parameters:
            rs - another list (List)
        Returns:
            identical - True if this list contains the same values 
                as other in the same order, otherwise False.
        -------------------------------------------------------
        """
        if( self._count == other._count ):
            identical = self._is_identical_r_aux(self._front, other._front)
            
        else:
            identical = False
        
        return identical
        
        
    def _is_identical_r_aux(self, key1, key2):
        if(key1 is None):
            result = True
            
        elif(key1._value == key2._value):
            result = self._is_identical_r_aux(key1._next, key2._next)
        
        else:
            result = False
        
        return result


    def split(self):
        """
        -------------------------------------------------------
        Splits list into two parts. target1 contains the first half,
        target2 the second half. Current list becomes empty.
        Use: target1, target2 = lst.split()
        -------------------------------------------------------
        Returns:
            target1 - a new List with >= 50% of the original List (List)
            target2 - a new List with <= 50% of the original List (List)
        -------------------------------------------------------
        """
        target1 = List()
        target2 = List()
        half = self._count // 2
        while(self._count > half):
            target1._move_front_to_rear(self)
        
        while(self._count > 0):
            target2._move_front_to_rear(self)
        
        return target1, target2


    def split_alt(self):
        """
        -------------------------------------------------------
        Splits the source list into separate target lists with values 
        alternating into the targets. At finish source list is empty.
        Order of source values is preserved.
        (iterative algorithm)
        Use: target1, target2 = source.split()
        -------------------------------------------------------
        Returns:
            target1 - contains alternating values from source (List)
            target2 - contains other alternating values from source (List)
        -------------------------------------------------------
        """
        target1 = List()
        target2 = List()
        alt = True
        while self._front is not None:
            if alt:
                target1._move_front_to_rear(self)
            else:
                target2._move_front_to_rear(self)

            
            alt = not alt
                
        return target1, target2


    def split_alt_r(self):
        """
        -------------------------------------------------------
        Split a list into two parts. even contains the even indexed
        elements, odd contains the odd indexed elements.
        Order of even and odd is not significant. (recursive version)
        Use: even, odd = lst.split_alt()
        -------------------------------------------------------
        Returns:
            even - the even numbered elements of the list (List)
            odd - the odd numbered elements of the list (List)
                The List is empty.
        -------------------------------------------------------
        """
        even = List()
        odd = List()
        self._split_alt_r_aux(even, odd)
        return even, odd
    

    def _split_alt_r_aux(self, even, odd):
        if(self._front is not None):
            even._move_front_to_rear(self)
            if(self._front is not None):
                odd._move_front_to_rear(self)  
                self._split_alt_r_aux(even, odd)
        
        return 


    def _linear_search_r(self, key):
        """
        -------------------------------------------------------
        Searches for the first occurrence of key in the list.
        Private helper methods - used only by other ADT methods.
        (recursive version)
        Use: p, c, i = self._linear_search(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            previous - pointer to the node previous to the node containing key (_List_Node)
            current - pointer to the node containing key (_List_Node)
            index - index of the node containing key, -1 if key not found (int)
        -------------------------------------------------------
        """
        return self._linear_search_r_aux(None, self._front, 0, key)
    

    def _linear_search_r_aux(self, prev, node, i, key):
        result = prev, None, -1
        if(node is not None):
            if(node._value == key):
                result = prev, node, i
            
            else:
                result = self._linear_search_r_aux(node, node._next, i + 1, key)
            
        
        return result 


    def intersection(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with values that appear in both
        source1 and source2. Values do not repeat.
        (iterative algorithm)
        Use: target.intersection(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        node = source1._front
        while(node is not None):
            if(node._value in source2 and node._value not in self):
                self.append(node._value)
            
            node = node._next
        
        return


    def intersection_r(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with values that appear in both
        source1 and source2. Values do not repeat.
        (recursive algorithm)
        Use: target.intersection(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        return self._intersection_r_aux(source1._front, source2)


    def _intersection_r_aux(self, node, source2):
        if(node is not None):
            if(node._value in source2 and node._value not in self):
                self.append(node._value)
            
            self._intersection_r_aux(node._next, source2)


    def union(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with all values that appear in
        source1 and source2. Values do not repeat.
        (iterative algorithm)
        Use: target.union(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        node = source1._front
        while(node is not None):
            if(node._value not in self):
                self.append(node._value)
            
            node = node._next
        
        node = source2._front
        while(node is not None):
            if(node._value not in self):
                self.append(node._value)
            
            node = node._next
        
        return


    def union_r(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with all values that appear in
        source1 and source2. Values do not repeat.
        (recursive algorithm)
        Use: target.union(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        self._union_r_aux(source1._front)
        self._union_r_aux(source2._front)        
        return
    
    
    def _union_r_aux(self, node):
        if(node is not None):
            if(node._value not in self):
                self.append(node._value)
                
            self._union_r_aux(node._next)

        return 
    

    def clean_r(self):
        """
        ---------------------------------------------------------
        Removes duplicates from the list. (recursive algorithm)
        Use: lst.clean_r()
        -------------------------------------------------------
        Returns:
            The list contains one and only one of each value formerly present
            in the list. The first occurrence of each value is preserved.
        -------------------------------------------------------
        """
        return self._clean_r_aux(self._front)

    
    def _clean_r_aux(self, node):
        return


    def split_th(self):
        """
        -------------------------------------------------------
        Splits list into two parts. target1 contains the first half,
        target2 the second half. Current list becomes empty.
        Uses Tortoise/Hare algorithm.
        Use: target1, target2 = lst.split()
        -------------------------------------------------------
        Returns:
            target1 - a new List with >= 50% of the original List (List)
            target2 - a new List with <= 50% of the original List (List)
        -------------------------------------------------------
        """
        target1 = List()
        target2 = List()
        
        return target1, target2


    def split_key(self, key):
        """
        -------------------------------------------------------
        Splits list so that target1 contains all values <= key,
        and target2 contains all values > key.
        Use: target1, target2 = lst.split_key(key)
        -------------------------------------------------------
        Parameters:
            key - a key value to split the list upon (?)
        Returns:
            target1 - a new List of values <= key (List)
            target2 - a new List of values > key (List)
        -------------------------------------------------------
        """
        target1, target2 = List(), List()
        while(self._count > 0):
            node = self._front
            if(node._value < key):
                target1._move_front_to_rear(self)
                
            else:
                target2._move_front_to_rear(self)
        
        return target1, target2


    def split_apply(self, func):
        """
        -------------------------------------------------------
        Splits list into two parts. target1 contains all the values 
        where the result of calling func(value) is True, target2 contains
        the remaining values. At finish, self is empty. Order of values 
        in targets is maintained.
        Use: target1, target2 = lst.split_apply(func)
        -------------------------------------------------------
        Parameters:
            func - a function that given a value in the list returns
                True for some condition, otherwise returns False.
        Returns:
            target1 - a new List with values where func(value) is True (List)
            target2 - a new List with values where func(value) is False (List)
        -------------------------------------------------------
        """
        target1, target2 = List(), List()
        while(self._count > 0):
            val = self._front._value
            if(func(val)):
                target1._move_front_to_rear(self)
        
            else:
                target2._move_front_to_rear(self)
        
        return target1, target2


    def copy(self):
        """
        -------------------------------------------------------
        Duplicates the current list to a new list in the same order.
        (iterative version)
        Use: new_list = lst.copy()
        -------------------------------------------------------
        Returns:
            new_list - a copy of self (List)
        -------------------------------------------------------
        """
        new_list = List()
        if(self._count > 0):
            a = self._front
            b = new_list._front = _List_Node(deepcopy(a._value), None)
            while(a._next is not None):
                a = a._next
                b._next = _List_Node(deepcopy(a._value), None)
                b = b._next
        
            new_list._rear = b
            new_list._count = self._count
        
        return new_list


    def copy_r(self):
        """
        -----------------------------------------------------------
        Duplicates the current list to a new list in the same order.
        (recursive verstion)
        Use: new_list = lst.copy()
        -----------------------------------------------------------
        Returns:
            new_list - a copy of self (List)
        -----------------------------------------------------------
        """
        return

    
    def reverse_pc(self):
        """
        -------------------------------------------------------
        Reverses a list through partitioning and concatenation.
        Use: lst.reverse_pc()
        -------------------------------------------------------
        Returns:
            The contents of the current list are reversed.
        -------------------------------------------------------
        """
        return


    def _move_front(self, rs):
        """
        -------------------------------------------------------
        Moves the front node from the rs List to the front
        of the current List. Private helper method.
        Use: self._move_front(rs)
        -------------------------------------------------------
        Parameters:
            rs - a non-empty linked List (List)
        Returns:
            The current List contains the old front of the rs List and
            its count is updated. The rs List front and count are updated.
        -------------------------------------------------------
        """
        assert rs._front is not None, "Cannot move the front of an empty List"
        temp = rs._front
        rs._front = rs._front._next
        temp._next = self._front
        self._front = temp

        rs._set_rear()
        self._set_rear()
        
        rs._count -= 1
        self._count += 1
        return


    def _move_front_to_rear(self, other):
        return self.append( other.remove_front() )
        
    
    def _set_rear(self):
        pointer = self._front
        if(pointer is None):
            self._rear = None
        
        else:
            while(pointer._next is not None):
                pointer = pointer._next
            
            self._rear = pointer
        
        return 

    
    def _find_node_index(self, node):
        pointer = self._front
        i = 0
        while(pointer is not None):
            if(pointer is node):
                return i
            
            i += 1
            pointer = pointer._next
            
        return -1
            
            

    def combine(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source lists into the current target list. 
        When finished, the contents of source1 and source2 are interlaced 
        into target and source1 and source2 are empty.
        Order of source values is preserved.
        (iterative algorithm)
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        alt = True
        while(source1._count > 0 or source2._count > 0):
            if(alt and source1._count > 0):
                self._move_front_to_rear(source1)
                
            elif(not alt and source2._count > 0):
                self._move_front_to_rear(source2)
        
            alt = not alt
        
        self._set_rear()
        return


    def combine_r(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source lists into the current target list. 
        When finished, the contents of source1 and source2 are interlaced 
        into target and source1 and source2 are empty.
        Order of source values is preserved.
        (recursive algorithm)
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - a linked list (List)
            source2 - a linked list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        return


    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the list
        from front to rear.
        Use: for v in s:
        -------------------------------------------------------
        Returns:
            yields
            value - the next value in the list (?)
        -------------------------------------------------------
        """
        current = self._front
        while current is not None:
            yield current._value
            current = current._next
        
        
l1 = List()
l1.append(11)
l1.append(55) 
l1.append(66)
l1.append(44) 
l1.append(33)
l1.append(22)
print([x for x in l1])
l1._swap(l1._front, l1._front._next)
print([x for x in l1])