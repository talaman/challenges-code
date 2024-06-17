#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'downToZero' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def downToZero(n):
    # Create a queue to store the numbers
    queue = [(n, 0)]
    # Create a set to store the visited numbers
    visited = set()
    while queue:
        num, steps = queue.pop(0)
        # If the number is 0, return the number of steps
        if num == 0:
            return steps
        # If the number is already visited, skip it
        if num in visited:
            continue
        # Add the number to the visited set
        visited.add(num)
        # Add the number - 1 to the queue
        queue.append((num - 1, steps + 1))
        # Add the factors of the number to the queue
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                queue.append((num // i, steps + 1))
    return 0

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = downToZero(n)

        fptr.write(str(result) + '\n')

    fptr.close()
