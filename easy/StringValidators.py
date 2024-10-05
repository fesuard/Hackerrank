# https://www.hackerrank.com/challenges/string-validators/problem
# You are given a string S.Your task is to find out if the string contains: alphanumeric characters, alphabetical
# characters, digits, lowercase and uppercase characters.
# In the first line, print True if S has any alphanumeric characters. Otherwise, print False.
# In the second line, print True if S has any alphabetical characters. Otherwise, print False.
# In the third line, print True if S has any digits. Otherwise, print False.
# In the fourth line, print True if S has any lowercase characters. Otherwise, print False.
# In the fifth line, print True if S has any uppercase characters. Otherwise, print False. 
import re


# using re
def string_validators(s):
    alphanum = bool(re.search(r'\w',s))
    letters = bool(re.search(r'[a-zA-Z]',s))
    digits = bool(re.search(r'[0-9]',s))
    lower = bool(re.search(r'[a-z]',s))
    upper = bool(re.search(r'[A-Z]',s))
    print(f"{alphanum}\n{letters}\n{digits}\n{lower}\n{upper}\n")


# using string validation
def string_validators1(s):
    res = [False] * 5
    for char in s:
        if char.isalnum():
            res[0] = True
        if char.isalpha():
            res[1] = True
        if char.isdigit():
            res[2] = True
        if char.islower():
            res[3] = True
        if char.isupper():
            res[4] = True
    for r in res:
        print(r)


if __name__ == '__main__':
    s = input()
    string_validators(s)
    
