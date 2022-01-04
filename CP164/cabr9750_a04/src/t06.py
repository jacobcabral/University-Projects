"""
-------------------------------------------------------
Assignment 4, Task 6
-------------------------------------------------------
Author:  Jacob Cabral
ID:      190689750
Email:   cabr9750@mylaurier.ca
__updated__ = "2020-02-01"
-------------------------------------------------------
"""
# Imports
from functions import prims
from functions import graph_test
from Graph import Edge, Graph
'''
#practice graph
data = (
    (['A', 'B'], 2), (['A', 'C'], 3), (['A', 'D'], 7), (['B', 'C'], 6),
    (['B', 'G'], 4), (['C', 'E'], 1), (['C', 'F'], 8), (['D', 'E'], 5),
    (['E', 'F'], 4), (['F', 'G'], 2)
)
'''
#assignment graph
data = (
    (['A', 'B'], 3), (['A', 'C'], 3), (['B', 'C'], 3), (['B', 'H'], 6),
    (['C', 'D'], 2), (['D', 'E'], 8), (['D', 'G'], 7), (['E', 'F'], 7),
    (['F', 'G'], 5), (['F', 'H'], 3), (['H', 'I'], 4)
)

edges = []
for d in data:
    edge = Edge(d[0], d[1])
    edges.append(edge)
    
graph = Graph(edges)

#inputC
start_node = input("Enter the start node: ").upper()

#calling the function
edges, total = prims(graph, start_node)

print()
#output:
print("Path:")
for edge in edges:
    s = str(edge)
    print(s)
print("Total Distance: {}".format(total))