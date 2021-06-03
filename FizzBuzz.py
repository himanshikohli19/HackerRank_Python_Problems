'''
FizzBuzz Problem:

Given a number n, for each integer i in the range from 1 to n inclusive, print
one value per line as follows:
- if i is a multiple of both 3 and 5, print FizzBuzz
- If i is multiple of 3 (but not 5) print Fizz.
- If i is multiple of 5 (but not 3) print Fizz.
- If i is not a multiple of 3 or 5, print value of i
'''

def fizzBuzz(n):
    for i in range(1,n+1):
        if i%3==0 and i%5==0:
            print("FizzBuzz")
        elif i%3==0:
            print("Fizz")
        elif i%5==0:
            print("Buzz")
        else:
            print(i)
    # Write your code here
if __name__ == '__main__':
    n = int(input().strip())

    fizzBuzz(n)
