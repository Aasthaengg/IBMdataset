import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0
n,a = map(int,readline().split())
lst1 = list(map(int,readline().split()))

import numpy as np

dp = np.zeros((n+1,3000),dtype=np.int64) # 枚数、目標数ごとに場合の数
dp[0,0] = 1

for x in lst1:
  dp[1:,x:] += dp[:-1,:-x].copy()
  
ans = 0
for i in range(1,n+1):
  ans += dp[i,i*a]
  
print(ans)
