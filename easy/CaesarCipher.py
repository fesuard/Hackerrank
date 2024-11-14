# Julius Caesar protected his confidential information by encrypting it using a cipher.
# Caesar's cipher shifts each letter by a number of letters. If the shift takes you past 
# the end of the alphabet, just rotate back to the front of the alphabet. In the case of 
# a rotation by 3, w, x, y and z would map to z, a, b and c.
# Original alphabet:      abcdefghijklmnopqrstuvwxyz
# Alphabet rotated +3:    defghijklmnopqrstuvwxyzabc
import math
import os
import random
import re
import sys


def caesarCipher(s, k):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
    hashm = {}
    s_list = list(s)
    
    for i in range(len(letters)):
        hashm[letters[i]] = numbers[i]
        
    for i in range(len(s_list)):
        up = False
        if s_list[i].isalpha():
            if s_list[i].isupper():
                up = True
            s_list[i] = s_list[i].lower()
            if hashm[s_list[i]] + k > 26:
                index = (hashm[s_list[i]] + k) % 26
                s_list[i] = letters[index-1]
                if up:
                    s_list[i] = s_list[i].upper()
            else:
                index = hashm[s_list[i]] + k
                s_list[i] = letters[index-1]
                if up:
                    s_list[i] = s_list[i].upper()
    
    return ''.join(s_list)
        
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
