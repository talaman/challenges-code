#!/bin/python3

import math
import os
import random
import re
import sys

# Objective
# Create a list, seqList, of N empty sequences, where each sequence is indexed from 0 to N - 1. The elements within each of the N sequences also use 0-indexing.
# Create an integer, lastAnswer, and initialize it to 0.
# The 2 types of queries that can be performed on your list of sequences (seqList) are described below:
# Query: 1 x y
# Find the sequence, seq, at index ((x ^ lastAnswer) % N) in seqList.
# Append integer y to sequence seq.
# Query: 2 x y
# Find the sequence, seq, at index ((x ^ lastAnswer) % N) in seqList.
# Find the value of element y % size in seq (where size is the size of seq) and assign it to lastAnswer.
# Print the new value of lastAnswer on a new line
# Task
# Given N, Q, and Q queries, execute each query.
# Note: ^ is the bitwise XOR operation, which corresponds to the ^ operator in most languages. Learn more about it on Wikipedia.
# Input Format
# The first line contains two space-separated integers, N (the number of sequences) and Q (the number of queries), respectively.
# Each of the Q subsequent lines contains a query in the format defined above.
# Constraints
# 1 <= N, Q <= 10^5
# 0 <= x <= 10^9
# 0 <= y <= 10^9
# It is guaranteed that query type 2 will never query an empty sequence or index.
# Output Format
# For each type 2 query, print the updated value of lastAnswer on a new line.
# Sample Input
# 2 5
# 1 0 5
# 1 1 7
# 1 0 3
# 2 1 0
# 2 1 1
# Sample Output
# 7
# 3
# Explanation
# Initial Values:
# N = 2
# lastAnswer = 0
# seqList = [[], []]
# Query 0: Append 5 to sequence ((0 ^ 0) % 2) = 0.
# seqList = [[5], []]
# lastAnswer = 0
# Query 1: Append 7 to

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
