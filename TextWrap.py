'''
You are given a string S and width W.
Your task is to wrap the string into a paragraph of width .

Function Description

Complete the wrap function in the editor below.

wrap has the following parameters:

string string: a long string
int max_width: the width to wrap to
Returns

string: a single string with newline characters ('\n')
where the breaks should be
'''

import textwrap

def wrap(string, max_width):
    len1=len(string)
    s1=""
    i=j=0
    while (i<len1):
        if (j<max_width):
            s1=s1+string[i]
            j+=1
            i+=1
        else:
            s1=s1+"\n"
            j=0      
    return s1

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
