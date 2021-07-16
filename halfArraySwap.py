#Swap half array to second half
#Ex: [1,2,3,4,5,6,7,8,9] ---> [5,6,7,8,9,1,2,3,4]

import numpy as np
x=[1,2,3,4,5,6,7,8,9]
a=np.array(x)
i=0
j=a.size-1
while(i<j):
    a[i],a[j]=a[j],a[i]
    i=i+1
    j=j-1
print(a)
