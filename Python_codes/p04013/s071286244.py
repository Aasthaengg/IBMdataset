N,A = map(int,input().split())
x = list(map(int,input().split()))
X = sum(x)

dp = [[[0 for k in range(X+1)] for j in range(N+1)] for i in range(N)]

for i in range(N):
    for j in range(i+1):
        dp[i][1][x[j]] += 1

for i in range(N-1):
    for j in range(1,i+2):
        for k in range(X+1):
            if 1 <= k-x[i+1] <= X:
                dp[i+1][j+1][k] = dp[i][j+1][k] + dp[i][j][k-x[i+1]]
            else:
                dp[i+1][j+1][k] = dp[i][j+1][k]

ans = 0
for j in range(1,N+1):
    if 1 <= A*j <= X:
        ans += dp[N-1][j][A*j]

print(ans)