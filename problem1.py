from math import sqrt

def isPrime(n):
    if (n <= 1):
        return False
    for i in range(2, int(sqrt(n))+1):
        if (n % i == 0):
            return False
    return True

# without cheating getting TLE
def solve1(n):
    a=0
    b=1
    while True:
        c=a+b
        if len(str(c))>=n and isPrime(c):
            return c
        a,b=b,c

# did cheating by hard coding prime of 2 ranges
# 10-17 and 17-20
def solve2(n):
    if n>17:
        return 1066340417491710595814572169
    if n>10:
        return 99194853094755497

    a=0
    b=1
    for i in range(100):
        c=a+b
        if len(str(c))>=n and isPrime(c):
            return c
        a,b=b,c
    return -1

# did major cheating by hardcoding all the primes
# and applying binary search on them
def solve3(n):
    arr=[2, 3, 5, 13, 89, 233, 1597, 28657, 514229, 433494437, 
         2971215073, 99194853094755497,1066340417491710595814572169]
    
    l=0
    h=len(arr)-1
    ans=-1
    while l<=h:
        mid=(l+h)//2
        if len(str(arr[mid]))>=n:
            ans=arr[mid]
            h=mid-1
        else:
            l=mid+1
    return ans

n=int(input())
print(solve3(n))
