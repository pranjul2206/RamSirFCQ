'''
using binary search
[2,5,4,3]
-step1 
    will be entering first element into our res[]
    res=[2]
-step2
    will try to find the place of next elemment 5 using binary seach
    found index=1
    we will shift all number to right from index
    res=[2,0]
    entering value at index
    res=[2,5]
-step3
    will try to find the place of next elemment 4 using binary seach
    found index=1
    we will shift all number to right from index
    res=[2,0,5]
    entering value at index
    res=[2,4,5]
-step4
    will try to find the place of next elemment 3 using binary seach
    found index=1
    we will shift all number to right from index
    res=[2,0,4,5]
    entering value at index
    res=[2,3,4,5]

total if conditions use in steps:
-step1=0
-step2=1
-step3=1
-step4=2
'''

import bisect
        
def rightShift(arr,index):
    i=len(arr)-1
    arr=arr[:index]+[0]+arr[index:]
    return arr

def solve(arr):
    res=[]
    for num in arr:
        if len(res)==0:
            res.append(num)
        else:
            index=bisect.bisect_left(res,num)
            res=rightShift(res,index)
            res[index]=num
    return res
    
arr=list(map(int,input().split()))
print(solve(arr))
