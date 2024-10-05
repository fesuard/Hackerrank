# https://www.hackerrank.com/challenges/python-string-split-and-join/problem
# You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen. 


def split_and_join(line):
    res = line.split()
    return "-".join(res)


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
