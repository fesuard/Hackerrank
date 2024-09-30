# https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem
# Maria plays college basketball and wants to go pro. Each season she maintains a record of 
# her play. She tabulates the number of times she breaks her season record for most points 
# and least points in a game. Points scored in the first game establish her record for the
# season, and she begins counting from there. Given the scores for a season, determine the 
# number of times Maria breaks her records for most and least points scored during the season.
import math
import os
import random
import re
import sys


def breakingRecords(scores):
    temp_scores = [scores[0],scores[0]]
    scores_count = [0,0]
    for score in scores:
        if score > temp_scores[0]:
            temp_scores[0] = score
            scores_count[0] += 1
        elif score < temp_scores[1]:
            temp_scores[1] = score
            scores_count[1] += 1
    return scores_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
