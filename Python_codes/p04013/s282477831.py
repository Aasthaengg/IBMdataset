import numpy as np
N, A = map(int, input().split())
X = [int(c) for c in input().split()]
dp = np.zeros((51,51,2501))
dp[:,0,0] = 1
for i in range(1,N+1):
  c = X[i-1]
  for k in range(1,N+1):
    dp[i,k,:c] = dp[i-1,k,:c]
    dp[i,k,c:] = dp[i-1,k,c:]+dp[i-1,k-1,:2501-c]
ans = 0
for i in range(1,N+1):
  ans += dp[N,i,i*A]
print(int(ans))
  
