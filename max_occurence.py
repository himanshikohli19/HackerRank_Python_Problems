#printing element with maximum occurence using dictionary
s = "abcabcbb"
dic = {}
for i in s:
    if i not in dic.keys():
        dic[i]=1
    else:
        dic[i]+=1
print(dic)
print(max(dic,key=dic.get))
