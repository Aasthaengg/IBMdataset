N, A = map(int, input().split())
X = list(map(int, input().split()))
for i in range(N):
    X[i] -= A
D = {0: 1}
for i in range(N):
    F = [[j, D[j]] for j in D]
    for j in F:
        if j[0] + X[i] in D:
            D[j[0] + X[i]] += j[1]
        else:
            D[j[0] + X[i]] = j[1]
print(D[0]-1)