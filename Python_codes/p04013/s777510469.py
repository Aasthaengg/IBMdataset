# 配列を大きめにとって配った方がすっきりかけるのかも

n, a = map(int, input().split())
x = list(map(int, input().split()))
X = max(max(x), a)
dp = [[[0]*(n*X+1) for _ in range(n+1)] for i in range(n+1)]

#if j == 0 and k == 0 and s == 0:
dp[0][0][0] = 1
for j in range(n):
    for k in range(n):
        for s in range(n*X):

            if dp[j][k][s]:
                dp[j+1][k][s] += dp[j][k][s]
                dp[j+1][k+1][s+x[j]] += dp[j][k][s]
ans = 0
for k in range(1,n+1):
    ans += dp[n][k][k*a]

print(ans)