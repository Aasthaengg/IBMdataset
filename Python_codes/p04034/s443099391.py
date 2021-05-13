n, m = map(int, input().split())
d = {i: [1, 0] for i in range(1, n+1)}
d[1][1] = 1
for _ in range(m):
    x, y = map(int, input().split())
    d[x][0] -= 1
    d[y][0] += 1
    if d[x][1] == 1:
        d[y][1] = 1
    if d[x][0] == 0:
        d[x][1] = 0
ans = sum(d[i][1] for i in range(1, n+1))
print(ans)
