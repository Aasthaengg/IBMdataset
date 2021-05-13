N, A = map(int,input().split())
X = list(map(int,input().split()))
dp = [[[0 for i in range(N*50+1)] for j in range(N+1)] for k in range(N+1)]
for i in range(N+1):
    dp[i][0][0] = 1
for i in range(1,N+1):
    x = X[i-1]
    for j in range(1,N+1):
        for k in range(N*50+1):
            if k < x:
                dp[i][j][k] = dp[i-1][j][k]
                
            elif j > i:
                dp[i][j][k] = 0
                
            else: 
                dp[i][j][k] += dp[i-1][j][k] + dp[i-1][j-1][k-x]
ans = 0
for i in range(1,N+1):
    ans += dp[N][i][A*i]
print(ans)
