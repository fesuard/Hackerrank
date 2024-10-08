# Complete the 'findSubstring' function below.
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
# It needs to return the substring of length k, with the most vowels


def findSubstring(s, k):
    n = len(s)
    string_list = []
    for i in range(n):
        if i + k <= n:
            string_list.append(s[i:i+k])
    res_list = sorted(string_list, key=lambda x: sum(x.count(vowel) for vowel in 'aeiou'), reverse=True)
    return res_list[0]
