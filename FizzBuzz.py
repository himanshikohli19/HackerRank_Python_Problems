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
#SPACE COMPLEXITY: O(1)
def FizzBuzzProblem(N):
    c4=0
    c5=0
    for i in range(1,N+1):
        c4+=1
        c5+=1
        r=''
        if (c4==4):
            r+='Fizz'
            c4=0

        if (c5==5):
            r+='Buzz'
            c5=0

        if r=='':
            print(i)

        else:
            print(r)

if __name__ == '__main__':
    n = 30
    FizzBuzzProblem(n)