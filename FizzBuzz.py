'''
FizzBuzz Problem:

Given a number n, for each integer i in the range from 1 to n inclusive, print
one value per line as follows:
- if i is a multiple of both 4 and 5, print FizzBuzz
- If i is multiple of 4 (but not 5) print Fizz.
- If i is multiple of 5 (but not 4) print Fizz.
- If i is not a multiple of 4 or 5, print value of i
'''
#TIME COMPLEXITY: O(N)

def FizzBuzzProblem(N):
    for i in range(1,N+1):
        if i%4==0 and i%5==0:
            print("FizzBuzz")
        elif i%4==0:
            print("Fizz")
        elif i%5==0:
            print("Buzz")
        else:
            print(i)
   
if __name__ == '__main__':
    n = 30
    FizzBuzzProblem(n)