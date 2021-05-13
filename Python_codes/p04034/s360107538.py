n, m = [int(_) for _ in input().split()]

ball = [1 for i in range(n)]
red = [False for i in range(n)]
red[0] = True

for i in range(m):
    x, y = [int(_)-1 for _ in input().split()]
    ball[x] -= 1
    ball[y] += 1
    if red[x]:
        red[y] = True
    if ball[x] == 0:
        red[x] = False

print(sum(red))
