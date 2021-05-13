N, A = map(int, input().split())
X = list(map(int, input().split()))
S = max(N * A, sum(X))
DP = [[[0] * (S+1) for _ in range(N+1)] for _ in range(N+1)]
DP[0][0][0] = 1
for i in range(N):
    for j in range(N+1):
        for k in range(S+1):
            if not DP[i][j][k]: continue
            DP[i+1][j][k] += DP[i][j][k]
            if j != N:
                DP[i+1][j+1][k+X[i]] += DP[i][j][k]
print(sum(DP[N][j][j*A] for j in range(1, N+1) if j * A <= S))