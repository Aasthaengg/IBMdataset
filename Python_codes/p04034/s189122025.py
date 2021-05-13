N, M = map(int, input().split())
Z = [list(map(int,input().split())) for i in range(M)]

B = [1 for i in range(N)]
R = [0 for i in range(N)]
R[0] = 1 #赤いボールが入っている可能性があるなら１、無いなら０
for i in range(M):
  src = Z[i][0]-1
  dst = Z[i][1]-1
  if B[src] > 1 and R[src] == 1:
    R[dst] = 1
  if B[src] == 1 and R[src] == 1:
    R[src] = 0 
    R[dst] = 1
  B[src] -= 1
  B[dst] += 1
print(sum(R))