import numpy as np

n,a = map(int, input().split())
X = np.array(input().split(), dtype=np.int64)
Y = X-a
U = max(X.max(), a) * n
dp = np.zeros(2*U+1, dtype=np.int64)
dp[U] = 1
for i in range(n):
  y = Y[i]
  if y >= 0:
    dp[y:] = dp[y:] + dp[:2*U+1-y]
  else:
    dp[:y] = dp[:y] + dp[-y:]
print(dp[U]-1)