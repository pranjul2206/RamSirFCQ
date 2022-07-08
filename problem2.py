# only using recursion
def solve1(n,divisor):
    if n==1:
        return
    i=divisor
    while i<=n:
        if n%i==0:
            print(i,end=' ')
            solve1(n//i,i)
            break
        i+=1

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
    i=divisor
    while i<=n:
        if n%i==0:
            print(i,end=' ')
            solve2(n//i,i)
            break
        i+=1
n=int(input())
solve2(n,2)
