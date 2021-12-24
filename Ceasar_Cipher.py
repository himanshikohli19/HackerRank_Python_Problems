'''
Caesar Cipher

Julius Caesar protected his confidential information by encrypting it
using a cipher. Caesar's cipher shifts each letter by a number of letters.
If the shift takes you past the end of the alphabet, just rotate back to the
front of the alphabet.
In the case of a rotation by 3, w, x, y and z would map to z, a, b and c.

Original alphabet:      abcdefghijklmnopqrstuvwxyz
Alphabet rotated +3:    defghijklmnopqrstuvwxyzabc
'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # Write your code here
    list1=[]
    alpha='abcdefghijklmnopqrstuvwxyz'
    nums='0123456789'
    symbols = {'~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/'}

    for i in s:
        if i in symbols or i in nums:
            list1.append(i)
            
        elif i.islower() and i in alpha:
            index=alpha.find(i)
            list1.append(alpha[(alpha.index(i)+k)%len(alpha)])
            
        elif i.isupper():
            i=i.lower()
            index=alpha.find(i)
            list1.append((alpha[(alpha.index(i)+k)%len(alpha)]).upper())
               
    str1=''.join(list1)
    return str1
            
            
                      

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
