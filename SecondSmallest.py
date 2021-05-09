L1=[18,21,2,4,7,9,18,5,2,1,0,3]
small=float('inf')
sec_small=float('inf')
for i in L1:
    if i<small:
        sec_small=small
        small=i
    elif i>small and i<sec_small:
        sec_small=i
print(small) #smallest
print(sec_small) #second smallest
    
