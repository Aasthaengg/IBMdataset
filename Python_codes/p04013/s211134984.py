N,A = map(int, input().split())
X = [int(x) for x in input().split()]

M = sum(X)
dp = [[[0]*(N+1) for _ in range(M+1)] for _ in range(N+1)]
    
for i in range(N+1):
    dp[i][0][0] = 1
    
for i in range(N):
    for j in range(M+1):
        for k in range(1, N+1):
            if j >= X[i]:
                dp[i+1][j][k] = dp[i][j][k] + dp[i][j-X[i]][k-1]
            else:
                dp[i+1][j][k] = dp[i][j][k]
        
ans = 0
for k in range(1, N+1):
    if k*A <= M:
        ans += dp[N][k*A][k]
            
print(ans)