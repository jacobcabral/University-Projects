Name: Jacob Cabral
ID: 190689750
Email: cabr9750@mylaurier.ca
WorkID: CP264-a8
Statement: I claim that the enclosed submission is my individual work.

Fill in the self-evaluation in the following evaluation grid.
Symbols: A - assignment, Q - question 
Field format: [self-evaluation/total marks/marker's evaluation]

For example, you put your self-evaluation, say 2, like [2/2/*]. 
If marker gives different evaluation value say 1, it will show 
[2/2/1] in the marking report. 

Evaluation grid: [self-evaluation/total/marker-evaluation]

A8

Q1 AVL tree
Q1.1 is_avl()                             [4/4/*]
Q1.2 rotate_left()                        [3/3/*]
Q1.3 rotate_right()                       [3/3/*]
Q1.4 insert()                             [5/5/*]
Q1.5 delete()                             [5/5/*]

Q2 AVL for marks data processing
Q2.1 merge_tree()                         [5/5/*]
Q2.2 merge_data()                         [5/5/*]

Total:                                   [30/30/*]

Copy and paste the console output of your public test in the following. This will help markers to evaluate your program if it fails the testing.  

Q1 output:


AVL insertion
insert(&root, A, 1.0):
|___A 1.0 1
is_val(&root):1

insert(&root, B, 2.0):
|___A 1.0 2
    |___B 2.0 1
is_val(&root):1

insert(&root, C, 3.0):
|___B 2.0 2
    |___C 3.0 1
    |___A 1.0 1
is_val(&root):1

insert(&root, D, 4.0):
|___B 2.0 3
    |___C 3.0 2
        |___D 4.0 1
    |___A 1.0 1
is_val(&root):1

insert(&root, E, 5.0):
|___B 2.0 3
    |___D 4.0 2
        |___E 5.0 1
        |___C 3.0 1
    |___A 1.0 1
is_val(&root):1

insert(&root, F, 6.0):
|___D 4.0 3
    |___E 5.0 2
        |___F 6.0 1
    |___B 2.0 2
        |___C 3.0 1
        |___A 1.0 1
is_val(&root):1

AVL deletion
delete(&root, A):
|___D 4.0 3
    |___E 5.0 2
        |___F 6.0 1
    |___B 2.0 2
        |___C 3.0 1
is_val(&root):1

delete(&root, C):
|___D 4.0 3
    |___E 5.0 2
        |___F 6.0 1
    |___B 2.0 1
is_val(&root):1

delete(&root, E):
|___D 4.0 2
    |___F 6.0 1
    |___B 2.0 1
is_val(&root):1



Q2 output:

Load data from file marks.txt.1
Bodnar         93.6
Chabot         80.4
Costa          45.1
Dabu           74.4
Giblett        59.1
Hatch          66.5
Myrie          76.7
Smith          60.1
Suglio         85.7
Sun            67.7

statistics summary
count:10
mean:70.9
stddev:13.5

Load data from file marks.txt.2
Ali            88.0
Allison        67.7
Eccles         77.8
He             85.7
Koreck         77.4
Lamont         98.1
Parr           92.5
Pereira        80.3
Peters         82.3
Wang           98.1

statistics summary
count:10
mean:84.8
stddev:9.2

Merge
Ali            88.0
Allison        67.7
Bodnar         93.6
Chabot         80.4
Costa          45.1
Dabu           74.4
Eccles         77.8
Giblett        59.1
Hatch          66.5
He             85.7
Koreck         77.4
Lamont         98.1
Myrie          76.7
Parr           92.5
Pereira        80.3
Peters         82.3
Smith          60.1
Suglio         85.7
Sun            67.7
Wang           98.1

statistics summary
count:20
mean:77.9
stddev:13.5

Write report to file report.txt

Read file report.txt
Ali,88.0,A
Allison,67.7,C
Bodnar,93.6,S
Chabot,80.4,A
Costa,45.1,F
Dabu,74.4,B
Eccles,77.8,B
Giblett,59.1,D
Hatch,66.5,C
He,85.7,A
Koreck,77.4,B
Lamont,98.1,S
Myrie,76.7,B
Parr,92.5,S
Pereira,80.3,A
Peters,82.3,A
Smith,60.1,C
Suglio,85.7,A
Sun,67.7,C
Wang,98.1,S

Statistics summary
count:20
mean:77.9
stddev:13.5
