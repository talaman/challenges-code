#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'checkMagazine' function below.
#
# The function accepts following parameters:
#  1. STRING_ARRAY magazine
#  2. STRING_ARRAY note
#

def checkMagazine(magazine, note):
    # Create a dict to store the frequency of each word
    freq = {}
    for i in magazine:
        freq[i] = freq.get(i, 0) + 1
    for i in note:
        # If the word is not in the dict or the frequency is 0
        # then we can't use the word
        if i not in freq or freq[i] == 0:
            print("No")
            return
        # Update the frequency of the word
        freq[i] -= 1
    print("Yes")
    return

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    m = int(first_multiple_input[0])

    n = int(first_multiple_input[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
