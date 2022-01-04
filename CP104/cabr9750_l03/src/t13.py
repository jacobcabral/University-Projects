"""
------------------------------------------------------------------------
[Takes the midterm mark and the final mark and calculates weighted average]
------------------------------------------------------------------------
Author: Jacob Cabral
ID:     190689750
Email:  cabr9750@mylaurier.ca
__updated__ = "2019-09-25"
------------------------------------------------------------------------
"""
MIDTERM_WEIGHT = 0.35
EXAM_WEIGHT = 0.65

midterm_score = float(input("Midterm mark (%): "))
exam_score = float(input("Exam mark (%): "))

weighted_average = (MIDTERM_WEIGHT * midterm_score) + (EXAM_WEIGHT * exam_score)

print("Final Grade (%): {:.1f}".format(weighted_average))