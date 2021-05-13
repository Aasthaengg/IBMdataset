n, a = map(int, input().split())
x = list(map(int, input().split()))
X = max(max(x), a)
#dp = [[[0]*(n*X+1) for _ in range(X+1)] for i in range(n+1)]
dp = [[[0]*(n*X+1) for _ in range(n+1)] for i in range(n+1)]

for j in range(n+1):
    for k in range(n+1):
        for s in range(n*X+1):
            if j == 0 and k == 0 and s == 0:
                dp[j][k][s] = 1
            elif j >= 1 and s < x[j-1]:
                dp[j][k][s] = dp[j-1][k][s]
            elif j >= 1 and k >= 1 and s >= x[j-1]:
                dp[j][k][s] = dp[j-1][k][s] + dp[j-1][k-1][s-x[j-1]]
            else:
                dp[j][k][s] = 0
ans = 0
for k in range(1,n+1):
    ans += dp[n][k][k*a]
print(ans)