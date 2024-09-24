# A Discrete Mathematics professor has a class of students. Frustrated with their lack of discipline, the professor decides 
# to cancel class if fewer than some number of students are present when class starts. Arrival times go from on time 
# (arrivalTime <= 0) to arrived late (arrivalTime > 0) Given the arrival time of each student and a threshhold number of 
# attendees, determine if the class is cancelled. 

import math
import os
import random
import re
import sys


def angryProfessor(k, a):
    count = sum(1 for arrival in a if arrival <= 0)
    if k > count:
        return 'YES'
    else:
        return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        a = list(map(int, input().rstrip().split()))

        result = angryProfessor(k, a)

        fptr.write(result + '\n')

    fptr.close()
