n, a = map(int, input().split())
x = list(map(int, input().split()))
X = max(max(x),a)
y = []
for i in x:
    y.append(i-a)
dp = [[0]*(2*n*X+1) for _ in range(n+1)]

for i in range(n+1):
    for j in range(len(dp[i])):
        if i == 0 and j == n * X:
            dp[i][j] = 1
        elif i > 0 and (j - y[i-1] < 0 or j - y[i-1] > 2 * n * X):
            dp[i][j] = dp[i-1][j]
        elif i > 0 and 0 <= j - y[i-1] <= 2 * n * X:
            dp[i][j] = dp[i-1][j] + dp[i-1][j-y[i-1]]
        else:
            dp[i][j] = 0

print(dp[n][n*X]-1)