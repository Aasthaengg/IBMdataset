n, m = [int(w) for w in input().split()]

lb = [False] * n
lb[0] = True
lbn = [1] * n

for i in range(m):
    x, y = [int(w)-1 for w in input().split()]
    if lb[x] and lbn[x] > 0:
        lb[y] = True
    lbn[x] -= 1
    lbn[y] += 1

    if lb[x] and lbn[x] == 0:
        lb[x] = False

print(len([_ for _ in lb if _]))
