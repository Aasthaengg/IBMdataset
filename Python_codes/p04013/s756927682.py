n,a=map(int,input().split())
lst=list(map(int,input().split()))

z=len(lst)
dp=[[[0]*2501 for i in range(51)] for j in range(z+1)]
dp[0][0][0]=1

for i in range(z):
  x=lst[i]
  for j in range(z):
    for k in range(2451):
      dp[i+1][j][k]+=dp[i][j][k]
      dp[i+1][j+1][k+x]+=dp[i][j][k]

ans=0

for i in range(z+1):
  ans+=dp[-1][i][i*a]

print(ans-1)