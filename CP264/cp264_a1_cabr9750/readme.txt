Name: Jacob Cabral
ID: 190689750
Email: cabr9750@mylaurier.ca
WorkID: CP264-a1
Statement: I claim that the enclosed submission is my individual work.

Fill in the self-evaluation in the following evaluation grid.
Symbols: A - assignment, Q - question 
Field format: [self-evaluation/total marks/marker's evaluation]

For example, you put your self-evaluation, say 2, like [2/2/*]. 
If marker gives different evaluation value say 1, it will show 
[2/2/1] in the marking report. 

Evaluation grid: [self-evaluation/total/marker-evaluation]

A1

Q1 Case flip
Q1.1 prompt for input                   [3/3/*]
Q1.2 input upper/lower case             [3/3/*]
Q1.3 robust for invalid input           [2/2/*]
Q1.4 repeat and quit                    [2/2/*]

Q2 Computing factorial
Q2.1 command line argument              [3/3/*]
Q2.2 correctness of computing           [2/3/*]
Q2.3 overflow testing                   [2/2/*]
Q2.4 output format                      [2/2/*]

Q3 Solving quadratic equation
Q3.1 correctness of computing           [6/6/*]
Q3.2 robust for invalid input           [2/2/*]
Q3.3 output format                      [2/2/*]
 
Total:                                  [29/30/*]

Comment:(optional)


Copy and paste the console output of your public test in the following. This will help markers to evaluate your program if it fails the testing.  

Q1 output:

C:\cp264\a1>gcc caseflip.c -o caseflip

C:\cp264\a1>caseflip
Please enter a character
a
a:97,A
Please enter a character
Z
Z:90,z
Please enter a character
$
$:invalid
Please enter a character
2
2:invalid
Please enter a character
*
*:quit


Q2 output:

C:\cp264\a1>gcc factorial.c -o factorial

C:\cp264\a1>factorial 6
          1          2          6         24
        120        720
6!:720

C:\cp264\a1>factorial 10
          1          2          6         24
        120        720       5040      40320
     362880    3628800
10!:3628800

C:\cp264\a1>factorial 15
          1          2          6         24
        120        720       5040      40320
     362880    3628800   39916800  479001600
overflow:13!

Q3 output:

C:\cp264\a1>gcc quadratic.c -o quadratic

C:\cp264\a1>quadratic
Please enter the coefficients a,b,c
1,2,1
The equation has two equal real roots
x:-1.000000
Please enter the coefficients a,b,c
1,2,2
The equation has two complex roots
real:-1.000000
imaginary:1.000000
Please enter the coefficients a,b,c
2,6,1
The equation has two distinct real roots
x1:-0.177124
x2:-2.822875
Please enter the coefficients a,b,c
0,1,2
input:not a quadratic equation
Please enter the coefficients a,b,c
a,a,a
input:Invalid input
Please enter the coefficients a,b,c
0,0,0
input:quit