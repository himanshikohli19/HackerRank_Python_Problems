'''
HackerRank in a string

We say that a string contains the word hackerrank if a
subsequence of its characters spell the word hackerrank.
Remeber that a subsequence maintains the order of characters
selected from a sequence.

More formally, let  be the respective
indices of h, a, c, k, e, r, r, a, n, k in string .
If  is true, then  contains hackerrank.

For each query, print YES on a new line if the string contains hackerrank,
otherwise, print NO.

'''
#!/bin/python3

import math
import os
import random
import re
import sys


def hackerrankInString(s):
    # Write your code here
    #s='hereiamstackerrank'
    str1 = 'hackerrank'
    i = 0
    for c in s:
        if c == str1[i]:
            i += 1
        if i == len(str1):
            break
             
    if i == len(str1):
        return "YES"
    else: 
        return "NO"
    
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        fptr.write(result + '\n')

    fptr.close()
