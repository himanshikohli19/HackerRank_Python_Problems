'''
PLUS MINUS
hackerrank.com/challenges/plus-minus/problem?isFullScreen=true

Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero.
 Print the decimal value of each fraction on a new line with 6 places after the decimal.
'''
#Solution
n = int(input().strip())
arr = [1 if int(num)>0 else -1 if int(num)<0 else 0 for num in input().strip().split(' ') ]
print("{0:.6f}".format(arr.count(1)/n))
print("{0:.6f}".format(arr.count(-1)/n))
print("{0:.6f}".format(arr.count(0)/n))
