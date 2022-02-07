'''
Write a Python program to check the validity of password input by users.
- At least 1 letter between [a-z] and 1 letter between [A-Z].
- At least 1 number between [0-9].
- At least 1 character from [$#@_^&*].
- Minimum length of 8 characters.
- Maximum length 16 characters.
'''

def PasswordValidity(n, password):

    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+_"
    cdigit=clower=cupper=cspchar=sum1=0

    if n>=8 and n<=16:
        for ch in password:
            if ch in numbers:
                cdigit+=1
            if ch in lower_case:
                clower+=1
            if ch in upper_case:
                cupper+=1
            if ch in special_characters:
                cspchar+=1

    if (cdigit>=1 and clower>=1 and cupper>=1 and cspchar>=1 and cdigit+clower+cupper+cspchar==n):
        return("Valid Password!")
    else:
        return("Invalid Password! Try Again.")
 
if __name__ == '__main__':
    password = input("Enter Password: ")
    n=len(password)
    answer = PasswordValidity(n, password)
    print(answer)

