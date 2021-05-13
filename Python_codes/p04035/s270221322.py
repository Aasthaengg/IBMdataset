import sys
input = sys.stdin.readline
N, L = map(int, input().split())
a = list(map(int, input().split()))
res = []
for i in range(N - 1):
  if a[i] + a[i + 1] >= L:
    res.append(i)
    break
else:
  print("Impossible")
  exit(0)
for i in range(res[0] - 1, -1, -1): res.append(i)
for i in range(res[0] + 1, N - 1): res.append(i)
res.reverse()
print("Possible")
for r in res: print(r + 1)