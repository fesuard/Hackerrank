# https://www.hackerrank.com/challenges/validating-credit-card-number/problem
# A valid credit card from ABCD Bank has the following characteristics:
# ► It must start with a 4, 5 or 6.
# ► It must contain exactly 16 digits.
# ► It must only consist of digits (0-9).
# ► It may have digits in groups of 4, separated by one hyphen "-".
# ► It must NOT use any other separator like ' ' , '_', etc.
# ► It must NOT have 4 or more consecutive repeated digits. 
# Verify if the card is valid.
import re


if __name__ == '__main__'":
    card_numbers = []
    for _ in range(int(input())):
        card_numbers.append(input())
    pattern1 = r'(?!.*(\d)\1{3})^[456][0-9]{15}$'
    pattern2 = r'(?!.*(\d)(-?\1){3})^[456]+[0-9]{3}-[0-9]{4}-[0-9]{4}-[0-9]{4}$'
    for card in card_numbers:
        if (re.match(pattern1, card) is not None) or (re.match(pattern2, card) is not None):
            print('Valid')
        else:
            print('Invalid')
