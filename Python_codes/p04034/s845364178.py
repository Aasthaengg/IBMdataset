n, m = map(int, input().split())

ball = [1] * n
flag = [1] + [0] * (n-1)

for _ in range(m):
    x, y = map(int, input().split())
    x, y = x-1, y-1

    ball[x] -= 1
    ball[y] += 1

    if flag[x] == 1:
        flag[y] = 1

    if ball[x] == 0:
        flag[x] = 0

print(sum(flag))