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
#from Food_utilities import read_food
from Stack_array import Stack
from Queue_array import Queue
from Priority_Queue_array import Priority_Queue
def array_to_stack(stack, source):
    """
    -------------------------------------------------------
    Pushes contents of source onto stack. At finish, source is empty.
    Last value in source is at bottom of stack,
    first value in source is on top of stack.
    Use: array_to_stack(stack, source)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while len(source) != 0:
        c = source.pop()
        stack.push(c)
        
    return

def stack_to_array(stack, target):
    """
    -------------------------------------------------------
    Pops contents of stack into target. At finish, stack is empty.
    Top value of stack is at end of target,
    bottom value of stack is at beginning of target.
    Use: stack_to_array(stack, target)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while stack.is_empty() != True:
        c = stack.pop()
        target.append(c)
        
    target.reverse()
    return target
        
def stack_test(source):
    """
    -------------------------------------------------------
    Tests the methods of Stack for empty and
    non-empty stacks using the data in source:
    is_empty, push, pop, peek
    (Testing pop and peek while empty throws exceptions)
    Use: stack_test(source)
    -------------------------------------------------------
    Parameters:
        source - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    s = Stack()
    
    for i in source:
        s.push(i)
        
    s.pop()
    s.peek()
    s.is_empty()
        
    return

def array_to_queue(queue, source):
    """
    -------------------------------------------------------
    Inserts contents of source into queue. At finish, source is empty.
    Last value in source is at rear of queue,
    first value in source is at front of queue.
    Use: array_to_queue(queue, source)
    -------------------------------------------------------
    Parameters:
        queue - a Queue object (Queue)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while(len(source) > 0):
        queue.insert(source.pop(0))

def queue_to_array(queue, target):
    """
    -------------------------------------------------------
    Removes contents of queue into target. At finish, queue is empty.
    Front value of queue is at front of target,
    rear value of queue is at end of target.
    Use: queue_to_array(queue, target)
    -------------------------------------------------------
    Parameters:
        queue - a Queue object (Queue)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while len(queue) > 0:
        target.append(queue.remove())
        
def array_to_pq(pq, source):
    """
    -------------------------------------------------------
    Inserts contents of source into pq. At finish, source is empty.
    Last value in source is at rear of pq,
    first value in source is at front of pq.
    Use: array_to_pq(pq, source)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue object (Priority_Queue)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    while (len(source) > 0):
        pq.insert(source.pop(0))

def pq_to_array(pq, target):
    """
    -------------------------------------------------------
    Removes contents of pq into target. At finish, pq is empty.
    Highest priority value in pq is at front of target,
    lowest priority value in pq is at end of target.
    Use: pq_to_array(pq, target)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue object (Priority_Queue)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    
    while (len(pq)>0):
        target.append(pq.remove())
        
def queue_test(a):
    """
    -------------------------------------------------------
    Tests queue implementation.
    Tests the methods of Queue are tested for both empty and
    non-empty queues using the data in a:
        is_empty, insert, remove, peek, len
    Use: queue_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    q = Queue()
    
    print("Calling is empty {}".format(q.is_empty()))
    print("Finding Length {}".format(len(q)))
    for i in range (len(a)):
        q.insert(a[i])
    print("Populated Queue")
    print("Calling is empty {}".format(q.is_empty()))
    print("finding length {}".format(len(q)))
    print("Calling Peek {}".format(q.peek()))
    print("Calling Remove {}".format(q.remove()))

    # tests for the queue methods go here
    # print the results of the method calls and verify by hand

    return


def priority_queue_test(a):
    """
    -------------------------------------------------------
    Tests priority queue implementation.
    Test the methods of Priority_Queue are tested for both empty and
    non-empty priority queues using the data in a:
        is_empty, insert, remove, peek
    Use: pq_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    pq = Priority_Queue()
    print("Calling is empty {}".format(pq.is_empty()))
    print("Finding Length {}".format(len(pq)))
    for i in range (len(a)):
        pq.insert(a[i])
    print("Populated Queue")
    print("Calling is empty {}".format(pq.is_empty()))
    print("finding length {}".format(len(pq)))
    print("Calling Peek {}".format(pq.peek()))
    print("Calling Remove {}".format(pq.remove()))

    # tests for the queue methods go here
    # print the results of the method calls and verify by hand

    

    return
        
        


    