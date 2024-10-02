# https://www.hackerrank.com/challenges/grading/problem
# Every student receives a grade in the inclusive range from 0 to 100.Any grade less than
# 40 is a failing grade.Sam is a professor at the university and likes to round each student's
# grade according to these rules: If the difference between the grade and the next multiple of
# 5 is less than 3, round grade up to the next multiple of 5. If the value of grade is less than
# 38, no rounding occurs as the result will still be a failing grade.
import math
import os
import random
import re
import sys


def gradingStudents(grades):
    res = []
    for grade in grades:
        if grade > 37:
            if grade % 5 > 2:
                new_grade = grade + (5-(grade%5))
                res.append(new_grade)
            else:
                res.append(grade)
        else:
            res.append(grade)
    return res   


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
