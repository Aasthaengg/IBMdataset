n, m = map(int, input().split())
red = [0 for _ in range(n)]
red[0] = 1
balls = [1 for _ in range(n)]
for _ in range(m):
    x, y = map(int, input().split())
    if balls[x-1]:
        balls[x-1] -= 1
        balls[y-1] += 1
        if red[x-1]:
            red[y-1] = 1
            if balls[x-1] == 0:
                red[x-1] = 0
cnt = 0
for i in range(n):
    if red[i] and balls[i]:
        cnt += 1
print(cnt)