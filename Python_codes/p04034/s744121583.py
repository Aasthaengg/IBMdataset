n, m = map(int, input().split())
l = [1 for i in range(n+1)]
b = [False for i in range(n+1)]
l[1] = 1
b[1] = True
for i in range(m):
    x, y = map(int, input().split())
    if b[x] == True:
        if l[x] == 1:
            b[x] = False
        b[y] = True
    l[x] -= 1
    l[y] += 1
cnt = 0
for i in range(1, n+1):
    if b[i] == True:
        cnt += 1
print(cnt)