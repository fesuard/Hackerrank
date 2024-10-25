# https://www.hackerrank.com/challenges/acm-icpc-team/problem
# Given a list of topics known by each attendee, presented as binary strings, determine the 
# maximum number of topics a 2-person team can know. Each subject has a column in the binary 
# string, and a '1' means the subject is known while '0' means it is not. Also determine the 
# number of teams that know the maximum number of topics. Return an integer array with two
# elements. The first is the maximum number of topics known, and the second is the number of
# teams that know that number of topics. 
import math
import os
import random
import re
import sys


def acmTeam(topic):
    n = len(topic)
    team_topics = []
      
    for i in range(n-1):
        for j in range(i+1, n):
            topics = 0
            for a, b in zip(topic[i], topic[j]):
                if a == '1' or b == '1':
                    topics += 1
            team_topics.append(topics)
                    
    return [max(team_topics), team_topics.count(max(team_topics))]
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

