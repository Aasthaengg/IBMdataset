def solve(n, m, x, y):
    x = list(map(lambda _:_-1, x))
    y = list(map(lambda _:_-1, y))
    p = [0] * n
    p[0] = 1
    c = [1] * n
    for i in range(m):
        if c[x[i]] > 1:
            if p[x[i]] == 1:
                p[y[i]] = 1
        else:
            if p[x[i]] == 1:
                p[y[i]] = 1
            p[x[i]] = 0
        c[x[i]] -= 1
        c[y[i]] += 1
    return sum(p)

n, m = map(int, input().split())
x = [0] * m
y = [0] * m
for i in range(m):
    x[i], y[i] = map(int, input().split())
print(solve(n, m, x, y))