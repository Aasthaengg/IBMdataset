N, A = map(int, input().split())
X = list(map(int, input().split()))

dp = [[[0]*(50*(N+1)+1) for _ in range(N+1)] for _ in range(N+1)]
dp[0][0][0] = 1

for i in range(N):
    for k in range(N):
        for s in range(50*N+1):
            dp[i+1][k][s] += dp[i][k][s]
            dp[i+1][k+1][s+X[i]] += dp[i][k][s]

ans = 0
for k in range(1, N+1):
    ans += dp[N][k][A*k]

print(ans)