#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    # Initialize the number of jumps
    jumps = 0
    # Initialize the current cloud index
    i = 0
    # Iterate through the clouds
    while i < len(c) - 1:
        # Check if it is possible to jump 2 clouds ahead and the next cloud is safe
        if i + 2 < len(c) and c[i + 2] == 0:
            # Jump 2 clouds ahead
            i += 2
        else:
            # Jump 1 cloud ahead
            i += 1
        # Increment the number of jumps
        jumps += 1
    # Return the total number of jumps
    return jumps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
