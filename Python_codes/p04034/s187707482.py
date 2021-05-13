N, M = list(map(int, input().split()))
xy = [list(map(int, input().split())) for _ in range(M)]

D = [0] * N
C = [1] * N
D[0] = 1

for x, y in xy:
  x -= 1
  y -= 1
  if D[x] == 1:
    D[y] = 1
  C[x] -= 1
  C[y] += 1
  if C[x] == 0:
    D[x] = 0

print(sum(D))