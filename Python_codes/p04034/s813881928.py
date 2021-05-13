N, M = map(int, input().split())
xy = [list(map(int, input().split())) for _ in range(M)]
red = [0] * (N+1) #赤になりうる場所を１とする
red[1] = 1
red[0] = ""
ball = [1] * (N+1) #個数
ball[0] = ""
for x, y in xy:
  ball[y] += 1
  ball[x] -= 1
  if red[x] == 1:
    red[y] = 1
    if ball[x] == 0: red[x] = 0
print(red.count(1))