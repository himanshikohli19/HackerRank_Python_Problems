#Given the names and grades for each student in a class of N students,
#store them in a nested list and print the name(s)
#of any student(s) having the second lowest grade.

#Note: If there are multiple students with the second lowest grade,
# order their names alphabetically and print each name on a new line.

matrix=[[input(),float(input())] for _ in range(int(input()))]

small=float('inf')
second_small=float('inf')
for name,score in matrix:
        if score<small:
                second_small=small
                small=score
        elif score>small and score<second_small:
                second_small=score

sorted_list=[] #sorted_list for names of second lowest student
for name,score in matrix:
    if score==second_small:
        sorted_list.append(name)

sorted_list.sort() #for sorting the names alphabetically
str1='\n'.join(map(str, sorted_list))
print(str1)





