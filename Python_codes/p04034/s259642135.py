n, m = map(int, input().split())

red = [False] * n
ball = [1] * n

red[0] = True
for _ in range(m):
    x, y = map(lambda x: int(x) - 1, input().split())
    if red[x]:
        red[y] = True
        if ball[x] == 1:
            red[x] = False
    ball[y] += 1
    ball[x] -= 1
print(len(list(filter(lambda x: x, red))))
