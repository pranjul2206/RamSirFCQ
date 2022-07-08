'''
time complexity-
O(n)--> for loop
O(n)--> min(x,y), gcd
total O(n^2)
it should pass the constraints i.e 1< N <999 
'''
def gcd(x,y):
    while y:
        x,y=y,x%y
    return x

def solve(n):
    count=1
    for i in range(2,n):
        if gcd(n,i)==1:
            count+=1
    return count
n=int(input())
print(solve(n))
