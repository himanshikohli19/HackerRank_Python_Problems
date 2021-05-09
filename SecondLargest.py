list1=[2,5,7,8,9,10,1,9,10,3,18,100,34,55,57,58,55,12,10,55,100,45]
large=-1
sec_large=-1
for i in list1:
    if i>large:
        sec_large=large
        large=i

    elif i<large and i>sec_large:
        sec_large=i    

print(sec_large)
    
