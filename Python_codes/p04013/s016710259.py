n, a = map(int, input().split())
x = list(map(int, input().split()))

dp = [[[0] * (n + 1) for _ in range(2501)] for _ in range(n + 1)]

dp[0][0][0] = 1
for i in range(1, n+1):
    for s in range(2501):
        for k in range(i):
            # no use
            dp[i][s][k] += dp[i-1][s][k]

            # use
            if s + x[i-1] <= 2500:
                dp[i][s + x[i-1]][k+1] += dp[i-1][s][k]

ans = 0
for k in range(1, n + 1):
    target = k * a
    ans += dp[-1][target][k]
print(ans)
