# https://www.hackerrank.com/challenges/find-a-string/problem
# In this challenge, the user enters a string and a substring. You have to print the number of times that
# the substring occurs in the given string. String traversal will take place from left to right, not from 
# right to left.
import re


# using finditer
def count_substring(string, sub_string):
    match = re.finditer(f'(?={sub_string})', string)
    return len(list(match))


# string slicing
def count_substring1(string, sub_string):
    n1 = len(string)
    n2 = len(sub_string)
    match = 0
    for i in range(n1-n2+1):
        if string[i:i+n2] == sub_string:
            match += 1
    return match


if __name__ == '__main__':
    string = input().strip()
    
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    
    print(count)
