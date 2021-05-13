n,m = map(int,input().split())
xyl = [list(map(int,input().split())) for nesya in range(m)]
red = [0]*n
ball = [1]*n
red[0] = 1
for xy in xyl:
  x = xy[0]-1
  y = xy[1]-1
  if red[x] > 0:
    red[y] = 1
    if ball[x] == 1:
      red[x] = 0
  ball[x] -= 1
  ball[y] += 1
print(sum(red))