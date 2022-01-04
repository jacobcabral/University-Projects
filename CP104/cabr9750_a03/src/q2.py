"""
------------------------------------------------------------------------
[Takes the midterm mark and the final mark and calculates if the user passes or fails cp104]
------------------------------------------------------------------------
Author: Jacob Cabral
ID:     190689750
Email:  cabr9750@mylaurier.ca
__updated__ = "2019-09-24"
------------------------------------------------------------------------
"""
midterm_mark = int(input("Enter your score in Midterm: (0-100): "))
final_exam_mark = int(input("Enter your score in Final: (0-100): "))

weighted_average = (0.2*midterm_mark) + (0.4*final_exam_mark)

print("Your weighted exam score is: {:.1f}".format(weighted_average))