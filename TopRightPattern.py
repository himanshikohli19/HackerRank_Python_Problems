#top right pattern
n=7
for i in range(1,8): 
    for j in range(1,n):
        if i>=j:
            print(" ",end=" ")
        else:
            print("*",end=" ")    
    print()


