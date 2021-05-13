#解説解答
n,a = map(int,input().split())
x = list(map(int,input().split()))
dp0 = [[0 for s in range(n*a+1)] for k in range(n+1)]
dp0[0][0] = 1
dp = dp0
for j in range(n):
  now = []
  for k in range(n+1):
    add = []
    for s in range(n*a+1):
      t = s-x[j]
      if t >= 0 and k >= 1:
        add.append( dp[k][s] + dp[k-1][t] )
      else:
        add.append( dp[k][s] )
    now.append(add)
  dp = now
ans = 0
for k in range(1,n+1):
  ans += dp[k][k*a]
print(ans)