N, A = map(int, input().split())
x = list(map(int, input().split()))
for i in range(N):
    x[i] -= A
max_x = max(max(x), A)

dp = [[0]*(2*N*max_x + 1) for i in range(N+1)]
dp[0][N*max_x] = 1

for i in range(N):
    for k in range(2*N*max_x + 1):
        dp[i+1][k] = dp[i][k]
        if 0 <= k - x[i] and k - x[i] <= 2*N*max_x:
            dp[i+1][k] += dp[i][k - x[i]]

print(dp[N][N*max_x] - 1)