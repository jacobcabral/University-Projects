Name: Jacob Cabral
ID: 190869750
Email: cabr9750@mylaurier.ca
WorkID: CP264-a9
Statement: I claim that the enclosed submission is my individual work.

Fill in the self-evaluation in the following evaluation grid.
Symbols: A - assignment, Q - question 
Field format: [self-evaluation/total marks/marker's evaluation]

For example, you put your self-evaluation, say 2, like [2/2/*]. 
If marker gives different evaluation value say 1, it will show 
[2/2/1] in the marking report. 

Evaluation grid: [self-evaluation/total/marker-evaluation]

A9

Q1 Chained hash table
Q1.1 new_node(), new_hashtable()          [3/3/*]
Q1.2 search()                             [3/3/*]
Q1.3 insert()                             [3/3/*]
Q1.4 delete()                             [3/3/*]

Q2 Symbolic expression evaluation
Q2.1 infix_to_postfix_symbol()            [5/5/*]
Q2.2 evaluate_infix_symbol()              [1/1/*]

Q3 Binary heap
Q3.1 new_heap(), find_index()             [3/3/*]
Q3.2 insert()                             [3/3/*]
Q3.3 extract_min()                        [3/3/*]
Q3.4 decrease_key()                       [3/3/*]

Total:                                   [30(?)/30/*]

Copy and paste the console output of your public test in the following. This will help markers to evaluate your program if it fails the testing.  

Q1 output:


hash table after insertion:ht1
size:  10
count: 8
hash data:
index: list of the data elements
 0: (d, 3)
 1: (e, 4)
 2: (f, 5)
 3: (g, 6)
 4: (h, 7)
 7: (a, 0)
 8: (b, 1)
 9: (c, 2)

search data by name:a
ht1 search result:(a, 0)
delete by name a:ht2
ht2 search result: not found
size:  10
count: 7
hash data:
index: list of the data elements
 0: (d, 3)
 1: (e, 4)
 2: (f, 5)
 3: (g, 6)
 4: (h, 7)
 8: (b, 1)
 9: (c, 2)
d=3
e=4
f=5
g=6
h=7
b=1
c=2


Q2 output:

Symbolic expressions:
a=5
b=3
c=(a+b)*(a-b)
b=a+b+c

Symbolic expression evaluation:
a=5
b=24
c=16


Q3 output:
size:0
capacity:4
(index, key, data):
insert to heap:
display heap after insertion:
size:10
capacity:16
(index, key, data): (0 4 10) (1 5 9) (2 8 6) (3 7 7) (4 6 8) (5 12 2) (6 9 5) (7 13 1) (8 10 4) (9 11 3)

the index of data value 6 is 2
decrease key value at index 2 to 2
size:10
capacity:16
(index, key, data): (0 2 6) (1 5 9) (2 4 10) (3 7 7) (4 6 8) (5 12 2) (6 9 5) (7 13 1) (8 10 4) (9 11 3)

call extract_min for 8 times:(2 6) (4 10) (5 9) (6 8) (7 7) (9 5) (10 4) (11 3)
display heap after extract min:
size:2
capacity:4
(index, key, data): (0 12 2) (1 13 1)