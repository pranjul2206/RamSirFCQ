import random
def setMine():
    totalMines=0
    while totalMines<k:
        num1=random.randint(0,m-1)
        num2=random.randint(0,n-1)
        if arr[num1][num2]=='*':
            continue
        else:
            arr[num1][num2]='*'
            totalMines+=1
            mines.append([num1,num2])

def Mark(i,j):
    for k in dir:
        ni=i+k[0]
        nj=j+k[1]
        if ni>=0 and ni<m and nj>=0 and nj<n and arr[ni][nj]!='*':
            arr[ni][nj]+=1

def printArr():
    for i in arr:
        for j in i:
            print(j,end='\t')
        print()

def solve():
    setMine()
    for mine in mines:
        Mark(mine[0],mine[1])
    printArr()

n,m,k=list(map(int,input().split()))
arr=[[0]*m for i in range(n)]
dir=[[0,1],[1,0],[-1,0],[0,-1],[1,1],[-1,-1],[1,-1],[-1,1]]
mines=[]
solve()
