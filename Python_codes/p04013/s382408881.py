n, a = map(int, input().split())
x = list(map(int, input().split()))

for i in range(n):
    x[i] -= a

dp = [0] * (2 * n * 50 + 2)
dp[0] = 1

for i in range(n):
    h = dp[:]
    for j in range(-(n - 1) * 50, (n - 1) * 50 + 1):
        h[j] += dp[j - x[i]]
    dp = h

print(dp[0] - 1)