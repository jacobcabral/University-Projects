"""
-------------------------------------------------------
Assignment 4, functions
-------------------------------------------------------
Author:  Jacob Cabral
ID:      190689750
Email:   cabr9750@mylaurier.ca
__updated__ = "2020-02-01"
-------------------------------------------------------
"""
# Imports
from Priority_Queue_array import Priority_Queue
from Graph import Edge
from Graph import Graph

#A4 T2
def pq_split_key(source, key):
    """
    -------------------------------------------------------
    Splits a priority queue into two depending on an external
    priority key. The source priority queue is empty when the method
    ends.
    Use: target1, target2 = pq_split_key(source, key)
    -------------------------------------------------------
    Parameters:
        source - a priority queue (Priority_Queue)
        key - a data object (?)
    Returns:
        target1 - a priority queue that contains all values
            with priority higher than key (Priority_Queue)
        target2 - priority queue that contains all values with
            priority lower than or equal to key (Priority_Queue)
    -------------------------------------------------------
    """
    target1 = Priority_Queue()
    target2 = Priority_Queue()
    
    while source.is_empty() == False:
        value = source.remove()
        if(value < key):
            target1.insert(value)
        elif(value >= key):
            target2.insert(value)
            
    return target1, target2

#A4 T4
def pq_split_alt(source):
    """
    -------------------------------------------------------
    Splits a priority queue into two with values going to alternating
    priority queues. The source priority queue is empty when the method
    ends. The order of the values in source is preserved.
    Use: target1, target2 = pq_split_alt(source)
    -------------------------------------------------------
    Parameters:
        source - a priority queue (Priority_Queue)
    Returns:
        target1 - a priority queue that contains alternating values
            from source (Priority_Queue)
        target2 - priority queue that contains  alternating values
            from source (Priority_Queue)
    -------------------------------------------------------
    """
    target1 = Priority_Queue()
    target2 = Priority_Queue()
    
    while source.is_empty() == False:
        if len(source) % 2 == 1:
            value = source.remove()
            target1.insert(value)
        elif len(source) % 2 == 0:
            value = source.remove()
            target2.insert(value)
        
    return target1, target2

#A4 T6
def graph_test(data):
    """
    -------------------------------------------------------
    Demonstrates use of Graph class. Prints
    all node names and edges in the graph
    Use: graph_test(data)
    -------------------------------------------------------
    Parameters:
        data - graph edges stored in tuples, where each tuple contains
            an edge [start, end], and distance (tuple of ([str, str], int))
    Returns:
        None
    -------------------------------------------------------
    """
    edges = []

    for d in data:
        edge = Edge(d[0], d[1])
        edges.append(edge)

    # Initialize the graph.
    graph = Graph(edges)

    node_names = graph.node_names()

    for node_name in node_names:
        print("Node: {}".format(node_name))
        node_edges = graph.edges_by_node(node_name)

        for edge in node_edges:
            print(edge)
        print()
    return

#A4 T6
def prims(graph, start_node):
    """
    -------------------------------------------------------
    Applies Prim's Algorithm to a graph.
    Use: edges, total = prims(graph, node)
    -------------------------------------------------------
    Parameters:
        graph - graph to evaluate (Graph)
        start_node - name of node to start evaluation from (str)
    Returns:
        edges - the list of the edges traversed (list of Edge)
        total - total distance of all edges traversed (int)
    -------------------------------------------------------
    """
    pq = Priority_Queue()
    nodes = []
    lines = []
    edges = []

    current_node = start_node  
   
    total = 0
    
    names = graph.node_names()   
    
    while(len(nodes) != len(names)):
        lines = graph.edges_by_node(current_node)
        for i in lines:
            if(i.start() not in nodes and i.end() not in nodes):
                pq.insert(i)
                  
        nodes.append(current_node)
        
        if(len(edges) != 0 and not pq.is_empty()):
            if(pq.peek().end() == edges[-1].end()):
                if (pq.peek() < edges[-1]):
                    edges.pop()
                else:
                    pq.remove()        
        
        value = pq.remove()
        if(value.end() not in nodes):
            edges.append(value)
            s = str(value)
            s.split(' ')
            total += int(s[-1])    
            
        current_node = edges[-1].end()
  
    return edges,total