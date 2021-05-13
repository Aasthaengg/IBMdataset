n,a = map(int,input().split())
x = [int(i) for i in input().split()]

sum_x = sum(x)

dp = [[[0 for i in range(n+1)]for j in range(sum_x+1)]for k in range(n+1)]

dp[0][0][0] = 1

for i in range(n):
    for j in range(n):
        for k in range(sum_x+1):
            dp[i+1][k][j] += dp[i][k][j]
            if k + x[i] > sum_x:
                continue
            dp[i+1][k+x[i]][j+1] += dp[i][k][j]
            
ans = 0

for i in range(n):
    if a*(i+1) > sum_x:
        break
    ans += dp[n][a*(i+1)][i+1]

print(ans)