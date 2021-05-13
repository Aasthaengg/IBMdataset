n, m, *XY = map(int, open(0).read().split())
A = [1] * n
B = [0] * n
B[0] = 1
for x, y in zip(XY[::2], XY[1::2]):
  x, y = x-1, y-1
  A[x] -= 1
  A[y] += 1
  if B[x]:
    B[y] = 1
  if A[x] == 0:
    B[x] = 0
print(sum(B))