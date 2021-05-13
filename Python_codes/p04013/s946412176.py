n,a = map(int,input().split())
x = list(map(int,input().split()))
for i in range(n):
    x[i] -= a
dp = [[0 for i in range(2*n*50+1)] for j in range(n+1)]
dp [0][n*50] = 1

for i in range(1,n+1):
    for j in range(2*n*50+1):
        if 0 <= j - x[i-1] < 2*n*50:
            dp[i][j] = dp[i-1][j] + dp[i-1][j-x[i-1]]
        else:
            dp[i][j] = dp[i-1][j]
    #print(dp[i])
print(dp[n][n*50] - 1) #全て選ばないを除く

# 4 8
# 7 9 8 9 のとき
# i = 1 で -1 0 が 1
# i = 2 で -1 1 が 1, 0 が2
# i = 3 で -1 1 が 2, 0 が4
# i = 4 で -1 2 が 2, 0 1 が 6