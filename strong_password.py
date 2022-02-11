#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
'''
STRONG PASSWORD

Louise joined a social networking site to stay in touch with her friends.
The signup page required her to input a name and a password.
However, the password must be strong.
The website considers a password to be strong if it satisfies the
following criteria:

Its length is at least 6.
It contains at least one digit.
It contains at least one lowercase English character.
It contains at least one uppercase English character.
It contains at least one special character.
The special characters are: !@#$%^&*()-+
She typed a random string of length n in the password field
but wasn't sure if it was strong. Given the string she typed,
can you find the minimum number of characters she must add to make
her password strong?
'''
#SOLUTION

def minimumNumber(n, password):
    
    min_num=0
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    cdigit=clower=cupper=cspchar=sum1=0
    for ch in password:
        if ch.isdigit():
            cdigit+=1
        if ch.islower():
            clower+=1
        if ch.isupper():
            cupper+=1
        if ch in special_characters:
            cspchar+=1
        
        lis = [cdigit,clower,cupper,cspchar]
        min_num=lis.count(0)
    
    return max(min_num,6-n)
 
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
