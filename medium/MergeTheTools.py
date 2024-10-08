# https://www.hackerrank.com/challenges/merge-the-tools/problem
# merge_the_tools has the following parameters:
#     string s: the string to analyze
#     int k: the size of substrings to analyze
# Print each subsequence on a new line. There will be n/k of them. No return value is expected.
# Input Format:
# The first line contains a single string, s.
# The second line contains an integer, k, the length of each substring.


def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        res = []
        for char in string[i:i+k]:
            if char not in res:
                res.append(char)
        print(''.join(res))


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
