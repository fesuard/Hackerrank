# https://www.hackerrank.com/challenges/re-start-re-end/submissions/code/353854332
# Your task is to find the indices of the start and end of string k in S.
import re


def substring_in_string(k, S):
    start_stop = []
    matches = re.finditer(f'(?={k})', S)
    for match in matches:
        start_stop.append(match.start())
        start_stop.append(match.start() + len(k) - 1)
    if len(start_stop) > 0:
        for i in range(0, len(start_stop), 2):
            print((start_stop[i], start_stop[i+1]))
    else:
        print((-1, -1))


if __name__ == '__main__':
    S = str(input())
    k = str(input())
    substring_in_string(k, S)
