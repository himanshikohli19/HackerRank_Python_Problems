#Given the names and grades for each student in a class of N students,
#store them in a nested list and print the name(s)
#of any student(s) having the second lowest grade.

#Note: If there are multiple students with the second lowest grade,
# order their names alphabetically and print each name on a new line.

matrix=[]
n=int(input())
for _ in range(n):
        name = input()
        score = float(input())
        list1=[]
        list1.append(name)
        list1.append(score)
        matrix.append(list1) #matrix creation [[]]
        
list2=[] #to store the scores
for i in range(n):
    score=matrix[i][1]
    list2.append(score)

list_unique=[] #creating a new score list with no score repeatition
[list_unique.append(k) for k in list2 if k not in list_unique]
list_unique.remove(min(list_unique))
second_least=min(list_unique)

list3=[] #list3 for names of second lowest student
for j in range(n):
    if matrix[j][1]==second_least:
        list3.append(matrix[j][0])

list3.sort() #for sorting the names alphabetically
str1='\n'.join(map(str, list3))
print(str1)
