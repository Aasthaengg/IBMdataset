N, M = map(int, input().split())
X, Y = [], []
d = {n:1 for n in range(N)}
r = set([0])
for _ in range(M):
    x, y = map(int, input().split())
    d[x-1] -= 1
    d[y-1] += 1
    if x - 1 in r:
        r.add(y - 1)
        if d[x - 1] == 0:
            r.remove(x - 1)
    X.append(x)
    Y.append(y)

print(len(r))