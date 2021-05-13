n, m = map(int,input().split())
ball = [1]*n
red_ball = [1] + [0]*(n-1)
for i in range(m):
  a,b = map(int,input().split())
  if red_ball[a-1] == 1:
    if ball[a-1] == 1:
      ball[a-1] -= 1
      ball[b-1] += 1
      red_ball[a-1] = 0
      red_ball[b-1] = 1
    else:
      ball[a-1] -= 1
      ball[b-1] += 1
      red_ball[b-1] = 1
  else:
    ball[a-1] -= 1
    ball[b-1] += 1
print(sum(red_ball))