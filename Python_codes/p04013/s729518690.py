n,a=map(int,input().split())
x=list(map(int,input().split()))
l=max(max(x)*n+3,a*n+3)
dp=[[l*[0]for _ in range(n+1)]for _ in range(n+1)]
dp[0][0][0]=1
for i in range(1,n+1):
  for j in range(i+1):
    for k in range(l):dp[i][j][k]=dp[i-1][j][k]
  for j in range(1,i+1):
    for k in range(x[i-1],l):dp[i][j][k]+=dp[i-1][j-1][k-x[i-1]]
ans=0
for j in range(1,n+1):
  ans+=dp[-1][j][j*a]
print(ans)
