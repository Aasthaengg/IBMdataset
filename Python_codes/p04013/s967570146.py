N, A = map(int, input().split())
x = list(map(int, input().split()))
dp = [[[0]*3000 for _ in range(N+1)] for _ in range(N+1)]
dp[0][0][0] = 1

for i in range(N):
    for j in range(N+1):
        for k in range(3000):
            dp[i+1][j][k] += dp[i][j][k]
            
            if j+1<=N and k+x[i]<3000:
                dp[i+1][j+1][k+x[i]] += dp[i][j][k]

ans = 0

for i in range(1, N+1):
    ans += dp[N][i][i*A]

print(ans)