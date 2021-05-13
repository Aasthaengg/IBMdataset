n, m = map(int, input().split())
checker = [1 for _i in range(n+1)]
r = [0 for i in range(n+1)]
r[1] = 1
for _i in range(m):
    x, y = map(int, input().split())
    checker[x] -= 1
    checker[y] += 1
    if r[x]>0:
        r[y] = 1
    if (r[x]>0) and (checker[x]==0):
        r[x] = 0
print(sum(r))