'''
A VERY BIG SUM - WARMUP HACKERRANK
https://www.hackerrank.com/challenges/a-very-big-sum/problem


In this challenge, you are required to calculate and print 
the sum of the elements in an array, keeping in mind that some of those integers may be quite large.


'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'aVeryBigSum' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER_ARRAY ar as parameter.
#

def aVeryBigSum(ar):
    # Write your code here
    x=0
    for i in range(0,len(ar)):
        x= x + ar[i]
    return x

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
