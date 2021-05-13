n, m = map(int, input().split())
used = [False] * (n+1)
ball = [1] * (n+1)
used[1] = True
for _ in range(m):
    x,y = map(int, input().split())
    ball[x] -= 1
    ball[y] += 1
    if used[x]:
        used[y] = True
    if ball[x] == 0:
        used[x] = False
res = 0
for i in range(1, n + 1):
    if used[i] and ball[i] != 0:
        res += 1
print(res)
#print(ball)
#print(used)