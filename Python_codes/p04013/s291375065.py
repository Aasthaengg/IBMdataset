import numpy as np
 
n, a = map(int, input().split())
x = np.array(list(map(int, input().split())))
 
dp = {0:1}
for y in x-a:
    for k, v in dp.copy().items():
        dp[y+k] = dp.get(y+k, 0) + v 
print(dp[0]-1)
