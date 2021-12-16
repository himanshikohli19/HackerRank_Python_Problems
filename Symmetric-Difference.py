'''
SYMMERTRIC DIFFERENCE

Task:
Given  sets of integers and, print their symmetric difference in ascending order.
The term symmetric difference indicates those values that exist
in either  or  but do not exist in both.

Input Format:
The first line of input contains an integer, .
The second line contains  space-separated integers.
The third line contains an integer, .
The fourth line contains  space-separated integers.

Output Format:
Output the symmetric difference integers in ascending order, one per line.
'''
#Solution
m=int(input())
a = list(map(int, input().split()))
n=int(input())
b = list(map(int, input().split()))
a=set(a)
b=set(b)
lis=sorted((a.union(b)).difference(a.intersection(b)))
for i in range(len(lis)):
    print(lis[i])
