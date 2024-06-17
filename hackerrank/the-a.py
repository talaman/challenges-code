#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    count_a = s.count('a')  # Count the number of 'a' in the string s
    repeat = n // len(s)  # Calculate how many times the string s repeats in n
    remaining = n % len(s)  # Calculate the remaining characters in n after repeating s
    count_a_remaining = s[:remaining].count('a')  # Count the number of 'a' in the remaining characters
    total_a = count_a * repeat + count_a_remaining  # Calculate the total number of 'a'
    return total_a

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
