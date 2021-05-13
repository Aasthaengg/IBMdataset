n, a = map(int, input().split())
x = list(map(int, input().split()))

# 初期化
max_num = max(max(x), a)
dp = [[[0 for _ in range(max_num * n + 1)]
       for _ in range(n + 1)] for _ in range(n + 1)]
dp[0][0][0] = 1

for j in range(1, n+1):
    for k in range(j+1):
        for s in range(max_num * k + 1):
            if s < x[j-1]:
                dp[j][k][s] = dp[j-1][k][s]
            elif k >= 1 and s >= x[j-1]:
                dp[j][k][s] = dp[j-1][k][s] + dp[j-1][k-1][s-x[j-1]]

ans = 0
for k in range(1, n+1):
    ans += dp[n][k][k*a]
print(ans)