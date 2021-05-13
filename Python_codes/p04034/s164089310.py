n, m = map(int, input().split())
num = [1] * n
red = [False] * n
red[0] = True
for _ in range(m):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    if red[x]:
        red[y] = True
    num[x] -= 1
    num[y] += 1
    if num[x] == 0:
        red[x] = False
ans = 0
for r in red:
    ans += r
print(ans)