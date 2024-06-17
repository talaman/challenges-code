#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countTriplets function below.
def countTriplets(arr, r):
    # Create a dict to store the frequency of each element
    freq = {}
    # Create a dict to store the frequency of each pair
    freqPairs = {}
    count = 0
    for i in reversed(arr):
        # If the element is the last element of the array
        # then there is no triplet
        if i * r in freqPairs:
            count += freqPairs[i * r]
        # If the element is in the frequency dict
        # then we need to update the frequency of the pair
        # with the next element
        if i * r in freq:
            freqPairs[i] = freqPairs.get(i, 0) + freq[i * r]
        # Update the frequency of the element
        freq[i] = freq.get(i, 0) + 1
    return count

if __name__ == '__main__':
    fptr = open('output.txt', 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()

