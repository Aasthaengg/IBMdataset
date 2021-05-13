N, K = map(int, input().split())
r = [False for _ in range(N+1)]
b = [1 for _ in range(N+1)]
r[1] = True
r_cnt = 1
for _ in range(K):
  x, y = map(int, input().split())
  b[x] -= 1
  b[y] += 1
  if r[x]:
    if b[x] == 0:
      r[x] = False
      r_cnt -= 1
    if not r[y]:
      r[y] = True
      r_cnt += 1
print(r_cnt)