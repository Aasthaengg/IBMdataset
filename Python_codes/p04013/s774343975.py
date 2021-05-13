N, A=map(int, input().split())
x=list(map(int, input().split()))

dp=[[[0]*2501 for j in range(N+1)] for i in range(N)]

dp[0][0][0]=1
dp[0][1][x[0]]=1
for i in range(1, N):
  dp[i][0][0]=1
  for j in range(1, i+2):
    for k in range(2501):
      if k-x[i]>=0:
        dp[i][j][k]=dp[i-1][j-1][k-x[i]]+dp[i-1][j][k]
      else:
        dp[i][j][k]=dp[i-1][j][k]
        
print(sum([dp[-1][j][A*j] for j in range(1, N+1)]))