n,a=map(int,input().split())
x=list(map(int,input().split()))
ans=0
dp=[[[0]*(sum(x)+1) for i in range(n+1)] for j in range(n+1)]
dp[0][0][0]=1
for i in range(n+1):
  for j in range(i+1):
    for k in range(sum(x)+1):
      if i>=1 and k>=x[i-1] and j>=1:
        dp[i][j][k]=dp[i-1][j-1][k-x[i-1]]+dp[i-1][j][k]
      elif i>=1:
        dp[i][j][k]=dp[i-1][j][k]
for j in range(1,n+1):
  for k in range(sum(x)+1):
    if k%j==0 and k//j==a:
      ans+=dp[n][j][k]
print(ans)
