# https://www.hackerrank.com/challenges/swap-case/problem
# You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.


def swap_case(s):
    res = ''
    for char in s:
        if char.isupper():
            char = char.lower()
        else:
            char = char.upper()
        res += char
    return res


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
