def solve(arr):
    arr.sort()
    condition1=arr[0]>0 and arr[1]>0 and arr[2]>0
    condition2=arr[2]**2 == arr[1]**2+arr[0]**2
    return condition1 and condition2

arr=list(map(int,input().split()))
print(solve(arr))
