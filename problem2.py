# only using recursion
def solve1(n,divisor):
    if n==1:
        return
    for i in range(divisor,n+1):
        if n%i==0:
            print(i,end=' ')
            solve1(n//i,i)
            break

# using recursion and prime function
from math import sqrt

def isPrime(n):
    if (n <= 1):
        return False
    for i in range(2, int(sqrt(n))+1):
        if (n % i == 0):
            return False
    return True

def solve2(n,divisor):
    if n==1:
        return
    if isPrime(n):
        print(n,end=' ')
        return
    for i in range(divisor,n+1):
        if n%i==0:
            print(i,end=' ')
            solve2(n//i,i)
            break

solve2(24,2)
