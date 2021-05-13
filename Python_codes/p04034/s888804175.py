n, m = map(int, input().split())
C = [0]*(n+1)
C[1] = 1
D = [1]*(n+1)
for _ in range(m):
  x, y = map(int, input().split())
  if C[x]:
    C[y] = 1
    if D[x] == 1:
      C[x] = 0
  D[x] -= 1
  D[y] += 1
ans = sum(C)
print(ans)