import numpy as np

N, A = map(int,input().split())
X = [int(x) for x in input().split()]
 
dp = np.zeros((N+1,N*A+1),dtype=np.int64)
dp[0,0] = 1
 
for x in X:
    dp[1:,x:] += dp[:-1,:-x].copy()
  
ans = 0
for n in range(1,N+1):
    ans += dp[n,n*A]

print(ans)