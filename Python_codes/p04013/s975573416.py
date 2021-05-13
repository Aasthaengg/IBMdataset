from collections import defaultdict
n, a = map(int, input().split())
x = list(map(int, input().split()))

dp = [defaultdict(int) for _ in range(n+1)]
dp[0][a] += 1

for i, x_i in enumerate(x):
    for p in dp[i].keys():
        pk = p + a - x_i
        dp[i+1][pk] += dp[i][p]
        dp[i+1][p] += dp[i][p]

print(dp[n][a] - 1)