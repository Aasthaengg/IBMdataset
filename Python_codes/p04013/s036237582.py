n, a = map(int, input().split())
x = list(map(int, input().split()))

m = a * n

# dp[i][j]: j 個使って合計がi
dp = [[0 for j in range(n+1)] for i in range(m+1)]
dp[0][0] = 1


for xk in x:
    # xkまで見たときを計算
    dpk = [dp[i][:] for i in range(m+1)]
    for i in range(m+1):
        if i - xk >= 0:
            for j in range(1,n+1):
                dpk[i][j] += dp[i-xk][j-1]
    dp = dpk

ans = 0

for i in range(1,m+1):
    for j in range(1,n+1):
        if i / j == a:
            ans += dp[i][j]

print(ans)