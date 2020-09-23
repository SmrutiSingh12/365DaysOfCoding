#!/bin/python3
#Problem Link:  https://www.hackerrank.com/challenges/grading/problem
import math
import os
import random
import re
import sys



def gradingStudents(grades):
    # Write your code here
    n=len(grades)
    for i in range(n):
        if grades[i]>=38:
            r=grades[i]%5
            if r>=3:
                grades[i]=grades[i]+(5-r)

    return grades           


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
