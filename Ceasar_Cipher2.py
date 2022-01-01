'''
Caesar Cipher -HackerRank
text

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
    str1=''
    for i in s:
        if i.islower():
            str1+= chr((ord(i)-97+k)%26+97)
            
        elif i.isupper():
            str1+= chr((ord(i)-65+k)%26+65)

        else:
            str1+=i
        return str1
    

#driver code
s,k=input(), int(input())
print(caesarCipher(s, k))
