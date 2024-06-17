#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'largestRectangle' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY h as parameter.
#

def largestRectangle(h):
    # Create a stack to store the indices of the heights
    stack = []
    # Create a variable to store the maximum area
    max_area = 0
    for i, height in enumerate(h):
        # If the stack is not empty and the current height is less than the height at the top of the stack
        while stack and h[stack[-1]] > height:
            # Calculate the area with the height at the top of the stack
            # and the width from the previous index to the current index
            top = stack.pop()
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, h[top] * width)
        stack.append(i)
    # Calculate the remaining areas in the stack
    while stack:
        top = stack.pop()
        width = len(h) if not stack else len(h) - stack[-1] - 1
        max_area = max(max_area, h[top] * width)
    return max_area

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()
