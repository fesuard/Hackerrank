# https://www.hackerrank.com/challenges/incorrect-regex/problem
# You are given a string S.
# Your task is to find out whether S is a valid regex or not.
# Print "True" or "False" for each test case without quotes.

import re
if __name__ == '__main__':
    def valid_regex(regex):
        try:
            re.compile(regex)
            return True
        except re.error:
            return False
    T = int(input())
    for _ in range(T):
        S = input()
        if valid_regex(S):
            print(True)
        else:
            print(False)
