#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    # Create a list of n empty lists
    seq_list = [[] for _ in range(n)]
    # Create a variable to store the last answer
    last_answer = 0
    # Create a list to store the answers
    answers = []
    for query in queries:
        # Get the query type, x, and y
        query_type, x, y = query
        # Calculate the index
        index = (x ^ last_answer) % n
        if query_type == 1:
            # Append y to the list at index
            seq_list[index].append(y)
        elif query_type == 2:
            # Get the value of y % size of the list at index
            size = len(seq_list[index])
            last_answer = seq_list[index][y % size]
            # Append the last answer to the answers list
            answers.append(last_answer)
    return answers

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
