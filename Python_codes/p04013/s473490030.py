N,A=map(int,input().split())
xlist=list(map(int,input().split()))

slist=[0]
for x in xlist:
  slist.append(slist[-1]+x)
#print(slist)

dp=[[[0]*(sum(xlist)+1) for _ in range(N+1)] for _ in range(N+1)]
dp[0][0][0]=1
for i in range(1,N+1):
  dp[i][0][0]=1
  for j in range(1,i+1):
    for k in range(1,slist[i]+1):
      dp[i][j][k]=dp[i-1][j][k]
      if k-xlist[i-1]>=0:
        dp[i][j][k]+=dp[i-1][j-1][k-xlist[i-1]]
#print(dp)

answer=0
for j in range(1,N+1):
  if j*A>sum(xlist):
    break
  answer+=dp[N][j][j*A]
  
print(answer)