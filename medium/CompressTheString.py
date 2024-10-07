# https://www.hackerrank.com/challenges/compress-the-string/problem
# You are given a string S. Suppose a character 'c' occurs consecutively X times in the string.
# Replace these consecutive occurrences of the character 'c' with (X,c) in the string. 
# Use groupby
import itertools


# using groupby
def grouping(s):
    res = []
    for key, group in itertools.groupby(s): 
        res.append((len(list(group)), int(key))) 
    print(*res)


if __name__ == '__main__':
    s = input()
    grouping(s)
