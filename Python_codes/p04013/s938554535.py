n, a = map(int, input().split())
x = list(map(int, input().split()))
x_max = max(x)
dp = [[[0]*(x_max*n+1) for k in range(n+1)] for i in range(n+1)]
ans = 0
dp[0][0][0] = 1
for i in range(n):
    for j in range(i+2):
        for k in range(x_max*n+1):
            if k>= x[i]:
                dp[i+1][j][k] = dp[i][j-1][k-x[i]] + dp[i][j][k]
            else:
                dp[i+1][j][k] = dp[i][j][k]
            
for k in range(x_max*n+1):
    for j in range(1,n+1):
        if a*j == k:
            ans += dp[n][j][k]
print(ans)