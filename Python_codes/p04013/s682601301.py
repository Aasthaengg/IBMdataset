import sys
import numpy as np
N, A = map(int, input().split())
X = np.array(list(map(int, input().split())))
x = X - A
R = 5001
dp = np.zeros([N, R], np.int64)
dp[0][(R-1)//2] += 1
dp[0][(R-1)//2 + x[0]] += 1

for i in range(1,N):
	for j in range(R):
		if 0 <= j-x[i] <= R-1:
			dp[i][j] = dp[i-1][j] + dp[i-1][j-x[i]]
		else:
			dp[i][j] = dp[i-1][j]
print(dp[N-1][(R-1)//2]-1)
