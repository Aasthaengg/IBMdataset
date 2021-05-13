N,M = map(int,input().split())
A = [0 for _ in range(N+1)]
B = [1 for _ in range(N+1)]
A[1] = 1
B[0] = 0
for _ in range(M):
    x,y = map(int,input().split())
    if A[x]==1:
        A[y]=1
    B[y] += 1
    B[x] -= 1
    if B[x]==0:
        A[x] = 0
print(sum(A))