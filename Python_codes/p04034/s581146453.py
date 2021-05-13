n, m = map(int,input().split())
num = [1 for i in range(n+1)]
red = [False for i in range(n+1)]
red[1] = True
for i in range(m):
  x, y = map(int,input().split())
  red[y] |= red[x]
  num[x] -= 1
  num[y] += 1
  if num[x] == 0:
    red[x] = False
print(red.count(True))