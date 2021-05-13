n, m = map(int, input().split())
xy = []
for _ in range(m):
    x, y = map(int, input().split())
    xy.append((x, y))
reds = [False]*n
reds[0] = True
balls = [1]*n
for x, y in xy:
    if reds[x-1] and balls[x-1]>1:
        reds[y-1] = True
    elif reds[x-1]:
        reds[y-1] = True
        reds[x-1] = False
    balls[x-1] -= 1
    balls[y-1] += 1
print(sum(reds))