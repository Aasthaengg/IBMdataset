N,M = map(int,input().split())
A = [[0]*N,[1]*N]
A[0][0] = 1
A[1][0] = 0

for i in range(M):
  x,y = map(int,input().split())
  if A[0][x-1] > 0:
    A[0][y-1] += 1
  else:
    A[1][y-1] += 1
  if A[1][x-1] > 0:
    A[1][x-1] -= 1
  else:
    A[0][x-1] -= 1
print(len([i for i in A[0] if i > 0]))