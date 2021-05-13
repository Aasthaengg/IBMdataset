n, m = map(int, input().split())
jud = [True] + [False]*(n - 1)
l = [1]*n

for i in range(m):
    x, y = map(int, input().split())
    x, y = x - 1, y - 1
    l[x] -= 1
    l[y] += 1
    if jud[x]:
        jud[y] = True
    if l[x] == 0:
        jud[x] = False

ans = 0
for i in jud:
    if i:
        ans += 1
print(ans)