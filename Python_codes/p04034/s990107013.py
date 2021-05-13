n, m = list(map(int, input().split()))
xy = [list(map(int, input().split())) for i in range(m)]

ans = [1] * (n)
ans[0] = 1
ball = [0] * (n)
ball[0] = 1
for i in range(m):
    x, y = xy[i]
    ans[y-1] += 1
    ans[x-1] -= 1
    if ball[x-1]:
      ball[y-1] = 1
    if ans[x-1] == 0:
      ball[x-1] = 0
      
print(sum(ball))