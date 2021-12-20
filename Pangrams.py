#!/bin/python3
'''
PANGRAM

A pangram is a string that contains every letter of the alphabet.
Given a sentence determine whether it is a pangram in the English alphabet.
Ignore case. Return either pangram or not pangram as appropriate.

Example
We promptly judged antique ivory buckles for the next prize

The string contains all letters in the English alphabet, so return pangram.

Function Description

Complete the function pangrams in the editor below. It should return the string pangram if the input string is a pangram. Otherwise, it should return not pangram.

pangrams has the following parameter(s):

string s: a string to test
Returns

string: either pangram or not pangram
Input Format

A single line with string .
'''

import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    #s='We promptly judged antique ivory buckles for the next prize'
    la='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    sp= ' '
    list1=list(la)+list(sp)
    for ch in s:
        ch=ch.upper()
        if ch in list1:
            list1.remove(ch)
   
    if len(list1) > 0:
        return "not pangram"
    else:
        return "pangram"           
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
