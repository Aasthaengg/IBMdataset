import numpy as np

N, A = map(int, input().split())
x = list(map(int, input().split()))
r = 0
l = 0
for y in x:
    y -= A
    if y < 0:
        l += y
    else:
         r += y

M = r-l+1
dp = np.zeros((N+1,M), dtype='i8')
dp[0][-l] = 1

for i in range(1, N+1):
    for j in range(M):
        dp[i][j] = dp[i-1][j]
        j2 = j-x[i-1]+A
        if 0 <= j2 and j2 < M:
            dp[i][j] += dp[i-1][j2]

print(dp[N][-l]-1)
