n, m = map(int, input().split())
counts = [1] * n
cands = [False] * n
cands[0] = True
for _ in range(m):
  x, y = map(lambda t: int(t) - 1, input().split())
  counts[x] -= 1
  counts[y] += 1
  if cands[x]:
    cands[y] = True
    if counts[x] == 0:
      cands[x] = False
print(sum(cands))