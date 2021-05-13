n, m = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(m)]

red = [False]*n
red[0] = True
balls = [1]*n

for x, y in mat:
    x -= 1
    y -= 1
    if red[x] is True:
        red[y] = True
    balls[x] -= 1
    balls[y] += 1
    if balls[x] == 0:
        red[x] = False

ans = 0
for r in red:
    if r is True:
        ans += 1
print(ans)