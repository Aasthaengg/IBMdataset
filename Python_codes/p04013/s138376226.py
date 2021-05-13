N, A = [int(x) for x in input().split()]
X = [int(x) for x in input().split()]

XX = sum(X) + 1

dp = [[[0 for i in range(XX * 2)] for i in range(N + 3)] for i in range(N + 3)]

dp[0][0][0] = 1

for i in range(N):
    for j in range(N + 1):
        for n in range(XX):
            dp[i + 1][j][n] += dp[i][j][n]
            dp[i + 1][j + 1][n + X[i]] += dp[i][j][n]

ans = 0
for i in range(1, N + 1):
    if i * A < XX:
        ans += dp[N][i][i * A]

print(ans)