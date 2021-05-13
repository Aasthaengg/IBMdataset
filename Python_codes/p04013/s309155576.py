N,A = map(int,input().split())
X = list(map(int,input().split()))
for i in range(N):
    X[i] -= A
dp = [[0 for i in range(5001)] for i in range(N+1)]
dp[0][2500] = 1
u = 2500
d = 2500
for i in range(1,N+1):
    x = X[i-1]
    if x <= 0:
        d += x
    else:
        u += x
    for j in range(d,u+1):
        dp[i][j] += dp[i-1][j-x] + dp[i-1][j]
print(dp[N][2500]-1)