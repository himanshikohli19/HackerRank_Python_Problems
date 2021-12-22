'''
Weighted Uniform Strings

https://www.hackerrank.com/challenges/weighted-uniform-string/problem
'''
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'weightedUniformStrings' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER_ARRAY queries
#

def weightedUniformStrings(s, queries):

    alpha = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8,'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26}
    
    sum_of_alpha =[]
    unique_alpha = []
    result=[] 
    for ch in range(len(s)):
        if s[ch] not in unique_alpha:
            unique_alpha.append(s[ch])
            sum_of_alpha.append(alpha[s[ch]])
        else:
            c=0
            i=ch
            while s[ch]==s[i]:
                c+=1
                i-=1 #backtracking
            sum_of_alpha.append((alpha[s[ch]])*c)

    for i in queries:
        if i in sum_of_alpha:
          result.append("Yes")
        else:
           result.append("No")
    return result
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
