N, A = [int(x_i) for x_i in input().split()]
x = [int(x_i) - A for x_i in input().split()]

X = max(x + [A])

dp=[[0] * (2*N*X + 1) for _ in range(N + 1)]

for j in range(N+1):
    for t in range(2*N*X):
        if j==0 and t==N*X:
            dp[j][t] = 1
        elif t-x[j-1] < 0 or t-x[j-1] > 2*N*X:
            dp[j][t] = dp[j-1][t]
        elif 0 < t-x[j-1] and t-x[j-1] < 2*N*X:
            dp[j][t] = dp[j-1][t] + dp[j-1][t-x[j-1]]
        else:
            dp[j][t] = 0

print(dp[N][N*X]-1)