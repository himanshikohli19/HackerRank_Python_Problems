'''
MINIMUM NUMBER

Given a number N and integer K, find the smallest possible number
that can be formed by deleting exactly K digits from N.
'''
n=int(input("Enter a number: "))
n=sorted(list(str(n)))
k=int(input("Enter a digits to be deleted: "))
listToStr= ''.join(map(str,n[0:k]))
print(listToStr)


