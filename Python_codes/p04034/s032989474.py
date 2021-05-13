N, M = map(int, input().split())
XY = [list(map(int, input().split())) for _ in range(M)]

status = [False]*N
status[0] = True
ball = [1]*N

for x, y in XY:
  x, y = x-1, y-1
  ball[x] -= 1
  ball[y] += 1
  if status[x]:
    status[y] = True
  if status[x] and ball[x] == 0:
    status[x] = False

print(sum(status))