#print first N prime numbers
n=int(input("Enter a number: "))
c=0
i=2
while (c<n):
    for j in range(2,i):
        if (i%j==0):
            i+=1
            break

    else:
        print(i)
        c+=1
        i+=1
    
    
