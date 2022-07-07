n,m=list(map(int,input().split()))
for i in range(n):
    for j in range(n):
        if abs(j-i)<=m:
            print('*',end=' ')
        else:
            print('0',end=' ')
    print()
