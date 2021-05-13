N, M = map(int,input().split())
red = [0] * N
red[0] = 1
boal = [1] * N

for i in range(M):
    x, y = map(int,input().split())
    x -= 1
    y -= 1
    if red[x] == 1 and boal[x] == 1:
        red[x] = 0
        boal[x] -= 1
        red[y] = 1
        boal[y] += 1
    elif red[x] == 1 and boal[x] > 1:
        boal[x] -= 1
        red[y] = 1
        boal[y] += 1
    else:
        boal[x] -= 1
        boal[y] += 1
print(sum(red))