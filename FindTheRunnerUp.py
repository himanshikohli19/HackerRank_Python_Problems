#Find the Runner-Up Score!
#HackerRank Problem
n = int(input())
arr = list(map(int, input().split()))
arr1=[]
[arr1.append(i) for i in arr if i not in arr1] #creating a new list removing all the duplicates
arr1.remove(max(arr1))#removing the maximum number from the list
print(max(arr1))

