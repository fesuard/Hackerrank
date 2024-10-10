# https://www.hackerrank.com/challenges/ginorts/problem
# Your task is to sort the string
# in the following manner:
#     All sorted lowercase letters are ahead of uppercase letters.
#     All sorted uppercase letters are ahead of digits.
#     All sorted odd digits are ahead of sorted even digits.


def custom_sort(s):
    res = ''
    lowercase = []
    uppercase = []
    digits = []
    for char in s:
        if char.islower():
            lowercase.append(char)
        elif char.isupper():
            uppercase.append(char)
        else:
            digits.append(char)
    lowercase.sort()
    uppercase.sort()
    digits = sorted(digits, key=lambda x: (int(x) % 2 == 0, int(x)))
    print("".join(lowercase + uppercase + digits))


if __name__ == '__main__':
    s = input()
    custom_sort(s)
