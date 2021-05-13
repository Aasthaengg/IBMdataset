# 全DP C - 高橋君とカード / Tak and Cards

import numpy as np

N, A = map(int, input().split())
x = np.array(list(map(int, input().split())))

x_diff = x - np.array(A)
X = max(A, max(x))

dp = np.zeros((N+2, 2*N*X+2)) #dp[i+1][j]はx_diff[i]までの数からいくつか選んで合計j-N*Xにするような選び方のパターン
dp = dp.tolist()
dp[0][N*X] = 1

for i in range(N):
    for j in range(2*N*X+1):
        if j < x_diff[i] or x_diff[i] < j - 2*N*X: # x_diff[i]を足しても絶対にj-N*Xにならないとき
            dp[i+1][j] = dp[i][j]
        else:
            dp[i+1][j] = dp[i][j] + dp[i][j-x_diff[i]]
            
print(int(dp[N][N*X] - 1))