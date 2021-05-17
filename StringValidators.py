#Python has built-in string validation methods for basic data. It can check if a string is
#composed of alphabetical characters, alphanumeric characters, digits, etc.
'''
You are given a string .
Your task is to find out if the string  contains: alphanumeric characters,
alphabetical characters, digits, lowercase and uppercase characters.
'''

if __name__ == '__main__':
    S = input()
    print(any(char.isalnum() for char in S))
    print(any(char.isalpha() for char in S))
    print(any(char.isdigit() for char in S))
    print(any(char.islower() for char in S))
    print(any(char.isupper() for char in S))
        
