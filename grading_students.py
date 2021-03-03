#!/bin/python3

import math
import os
import random
import re
import sys

#
# Solution of Grading Students problem in Problem Solving challenge on HackerRank
#

def gradingStudents(grades):
    
    final_grades = list()
    
    for i in range(len(grades)):
        
        if grades[i]<38:
            final_grades.insert(i,grades[i])
    
        else:
            a = grades[i]//5

            if ((a+1)*5-grades[i]<3):
                final_grades.insert(i,(a+1)*5)
            else:
                final_grades.insert(i,grades[i])
            
    return final_grades
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
