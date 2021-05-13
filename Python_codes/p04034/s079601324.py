n,m = map(int, input().split())
xy = []

for i in range(m):
  x,y = map(int, input().split())
  xy.append([x-1,y-1])

box = [1 for i in range(n)]

chk = [False for i in range(n)]
chk[0] = True
for i in range(m):
  x, y = xy[i][0],xy[i][1]
  if chk[x]:
    if box[x] >= 2:
      chk[y] = True 
    else:
      chk[y] = True
      chk[x] = False
  box[y] += 1
  box[x] -= 1
cnt = 0
for i in range(n):
  cnt += chk[i]
print (cnt)