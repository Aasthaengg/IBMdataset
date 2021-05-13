N,A=map(int,input().split())
x = list(map(int,input().split()))
y = [val-A for val in x]

# dp[i][j] : i枚目まで見て合計がj-2500のもの
dp = [[0]*5001 for _ in range(N+1)]
dp[0][y[0]+2500] = 1
dp[0][2500] += 1
for i in range(N-1):
    new = y[i+1]
    for j in range(5001):
        dp[i+1][j] += dp[i][j]
        if 0 <= j+new <= 5000:
            dp[i+1][j+new] += dp[i][j]
print(dp[N-1][2500]-1)
