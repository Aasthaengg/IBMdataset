from collections import defaultdict
n, m = map(int, input().split())
r = set()
r.add(1)
d = defaultdict(int)
for i in range(m):
  x, y = map(int, input().split())
  d[x] -= 1
  d[y] += 1
  if x in r:
    r.add(y)
  if d[x] == -1 and x in r:
    r.remove(x)
ans = len(list(r))
for e in d:
  if d[e] == -1 and e in r:
    ans -= 1
print(ans)