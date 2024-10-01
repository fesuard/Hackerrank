# https://www.hackerrank.com/challenges/designer-pdf-viewer/problem
# When a contiguous block of text is selected in a PDF viewer, the selection is highlighted with a blue rectangle.
# In this PDF viewer, each word is highlighted independently.There is a list of 26 character heights aligned by index
# to their letters. For example, 'a' is at index 0 and 'z' is at index 25. There will also be a string. Using the 
# letter heights given, determine the area of the rectangle highlight in mm^2 assuming all letters are 1mm wide. 
import math
import os
import random
import re
import sys
import string


def designerPdfViewer(h, word):
    hashm = {}
    letters = string.ascii_lowercase
    for i in range(len(letters)):
        hashm[letters[i]] = h[i]
    max_height = max(hashm[l] for l in word)
    return max_height * len(word)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()
