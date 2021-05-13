n, m = list(map(int, input().split()))
xy = [list(map(int, input().split())) for i in range(m)]

ans = [1] * (n)
ans[0] = 1
ball = [False] * (n)
ball[0] = True
for i in range(m):
    x, y = xy[i]
    ans[y-1] += 1
    ans[x-1] -= 1
    if ball[x-1]:
      ball[y-1] = True
    if ans[x-1] == 0:
      ball[x-1] = False
      
cnt = 0
for i in ball:
  if i:
    cnt += 1

print(cnt)