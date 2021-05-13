N,M = map(int,input().split())
A = [[0,1] for _ in range(N)]
A.insert(0,[0,0])
A[1][0] = 1
for _ in range(M):
    x,y = map(int,input().split())
    A[y][1] += 1
    if A[x][0]==1:
        A[y][0]=1
    A[x][1] -= 1
    if A[x][1]==0:
        A[x][0]=0
cnt = 0
for i in range(1,N+1):
    cnt += A[i][0]
print(cnt)