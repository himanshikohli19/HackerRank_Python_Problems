'''
NO IDEA!

There is an array of  integers. There are also  disjoint sets,
and , each containing  integers. You like all the integers in set  and
dislike all the integers in set . Your initial happiness is .
For each  integer in the array, if , you add  to your happiness.
If , you add  to your happiness. Otherwise, your happiness does not change.
Output your final happiness at the end.

Note: Since  and  are sets, they have no repeated elements.
However, the array might contain duplicate elements.


Input Format
The first line contains integers  and  separated by a space.
The second line contains  integers, the elements of the array.
The third and fourth lines contain  integers,  and , respectively.

Output Format
Output a single integer, your total happiness.
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m = map(int, input().split())
Arr = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))
hap=0
for i in range(len(Arr)):
    if Arr[i] in A:
        hap+=1
    if Arr[i] in B:
        hap-=1
print(hap)



