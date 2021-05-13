n,m=map(int,input().split())
dp=[False]*n
dp2=[1]*n

dp[0]=True

for i in range(m):
  x,y=map(int,input().split())
  x-=1
  y-=1
  dp2[y]+=1
  if dp[x]==True:
    dp[y]=True
    
  dp2[x]-=1
  if dp2[x]==0:
    dp[x]=False
    
ans=0

for i in range(n):
  if dp[i]==True:
    ans+=1
    
    
print(ans)