N,M = map(int,input().split())
C = {i:[0,1] for i in range(1,N+1)}
C[1] = [1,1]
for _ in range(M):
    x,y = map(int,input().split())
    if C[x][0]==1:
        C[y][0]=1
    C[y][1] += 1
    C[x][1] -= 1
    if C[x][1]==0:
        C[x][0]=0
cnt = 0
for i in range(1,N+1):
    if C[i][0]==1:
        cnt += 1
print(cnt)