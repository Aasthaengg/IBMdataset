n, m = map(int, input().split())

r = [False] * n
r[0] = True
l = [1] * n

for _ in range(m):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    l[x] -= 1
    l[y] += 1
    r[y] = r[x] | r[y]
    if not l[x]:
        r[x] = False

c = 0
for i in range(n):
    if r[i] == True and l[i] > 0:
        c += 1

print(c)
