N,M = map(int,input().split())
R,A = [0]*N,[1]*N
R[0] = 1
for i in range(M):
    x,y = map(int,input().split())
    x,y = x-1,y-1
    if A[x] > 1 and R[x] == 1:
        R[y] = 1
    elif A[x] ==  R[x] == 1:
        R[x] = 0
        R[y] = 1
    A[x] -= 1
    A[y] += 1
print(sum(R))