'''
Write a Python program to check the validity of password input by users.
- At least 1 letter between [a-z] and 1 letter between [A-Z].
- At least 1 number between [0-9].
- At least 1 character from [$#@_^&*].
- Minimum length of 8 characters.
- Maximum length 16 characters.
'''
#TIME COMPLEXITY: O(N)

def PasswordValidity(n, password):

    special_characters = "!@#$%^&*()-+_"
    cdigit=clower=cupper=cspchar=0 #initializing counters

    if n>=8 and n<=16:
        for ch in password:
            if ch.isdigit():
                cdigit+=1
            if ch.islower():
                clower+=1
            if ch.isupper():
                cupper+=1
            if ch in special_characters:
                cspchar+=1

    if (cdigit>=1 and clower>=1 and cupper>=1 and cspchar>=1 and cdigit+clower+cupper+cspchar==n):
        return("Valid Password!")
    else:
        return("Invalid Password! Try Again.")
 
#Driver Code
if __name__ == '__main__':
    password = input("Enter Password: ")
    n=len(password) #n stores the length of the input password
    answer = PasswordValidity(n, password) # Function Call
    print(answer)

