# Implement a function that takes a string that consists of lowercase letters and digits and returns a
# string that consists of all digits and lowercase English letters that are not present in the string.
# The digits should come first, in ascending order, followed by characters, also in ascending order.
import string


def missing_characters(s):
    all_letters = set(string.ascii_lowercase)
    all_digits = set(string.digits)
    set_s = set(s)
    res_letters = sorted(all_letters - set_s)
    res_digits = sorted(all_digits - set_s)
    return ''.join(res_digits + res_letters)

if __name__ == '__main__':
    s = input().strip()
    print(missing_characters(s))
    
