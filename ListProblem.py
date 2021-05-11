#Consider a list (list = []). You can perform the following commands:
#1. insert i e: Insert integer e at position i.
#2. print: Print the list.
#3. remove e: Delete the first occurrence of integer e.
#4. append e: Insert integer e at the end of the list.
#5. sort: Sort the list.
#6. pop: Pop the last element from the list.
#7. reverse: Reverse the list.

#Initialize your list and read in the value of n followed by n lines of commands where each command will be of the  types listed above. Iterate through
#each command in order and perform the corresponding operation on your list.

if __name__ == '__main__':
    n=int(input())
    list1=[]
    for _ in range(n):
        str1=input()
        action,*num=str1.split() #taking input as str and list
        if action == 'insert':
            list1.insert(int(num[0]),int(num[1])) #element and index
        elif action == 'append':
            list1.append(int(num[0])) #element at the end
        elif action == 'print':
            print(list1)
        elif action == 'sort':
            list1.sort()
        elif action == 'remove':
            list1.remove(int(num[0])) #element
        elif action == 'reverse':
            list1.reverse()
        elif action == 'pop':
            list1.pop()
    
