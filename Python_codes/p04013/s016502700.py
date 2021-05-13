N, A = map(int, input().split())
X = list(map(int, input().split()))
Y = [x - A for x in X]
LMT = max(max(X), A)

dp = [[0 for _ in range(2 * N * LMT + 1)] for _ in range(N + 1)]
 
for j in range(N + 1) :
    for t in range(2 * N * LMT + 1):
        if j == 0 and t == N * LMT:
            dp[j][t] = 1
        elif j >= 1 and (t - Y[j - 1] < 0 or t - Y[j - 1] > 2 * N * LMT):
            dp[j][t] = dp[j - 1][t]
        elif j >= 1 and (0 <= t - Y[j - 1] <= 2 * N * LMT):
            dp[j][t] = dp[j - 1][t] + dp[j - 1][t - Y[j - 1]]
        else:
            dp[j][t] = 0
print(dp[N][N*LMT]-1)