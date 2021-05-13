n, m = map(int, input().split())

X = [0]*n
C = [1]*n
X[0] = 1

for i in range(m):
    x, y = map(int, input().split())
    x, y = x-1, y-1
    if X[x] == 1:
        X[y] = 1
        if C[x] == 1:
            X[x] = 0
        C[x] -= 1
        C[y] += 1
    else:
        C[x] -= 1
        C[y] += 1

ans = sum(X)
print(ans)
