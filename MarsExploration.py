'''
MARS EXPLORATION

A space explorer's ship crashed on Mars!
They send a series of SOS messages to Earth for help.

NASA_Mars_Rover.jpg

Letters in some of the SOS messages are altered by cosmic radiation
during transmission. Given the signal received by Earth as a string,
determine how many letters of the SOS message have been changed by radiation.

Example


The original message was SOSSOS.
Two of the message's characters were changed in transit.

Function Description

Complete the marsExploration function in the editor below.

marsExploration has the following parameter(s):

string s: the string as received on Earth
Returns

int: the number of letters changed during transmission
Input Format

There is one line of input: a single string, .


 will contain only uppercase English letters, ascii[A-Z].

Sample Input 0
SOSSPSSQSSOR

Sample Output 0
3
'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the 'marsExploration' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def marsExploration(s):
    # Write your code here
    c=0
    lis = [s[i:i+3] for i in range(0,len(s),3)]
    for ch in lis:
        if ch[0] !='S':
            c+=1
        if ch[1]!='O':
            c+=1
        if ch[2]!='S':
            c+=1
    return c
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
