import sys
input = sys.stdin.buffer.readline
N, L = map(int, input().split())
a = list(map(int, input().split()))
res = []
for i in range(N - 1):
  if a[i] + a[i + 1] >= L:
    res.append(i + 1)
    break
if len(res):
  i = res[0] - 1
  while i > 0:
    res.append(i)
    i -= 1
  i = res[0] + 1
  while i < N:
    res.append(i)
    i += 1
  print("Possible")
  for i in range(N - 2, -1, -1):
    print(res[i])
else:
  print("Impossible")