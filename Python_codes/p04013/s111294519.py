n,a=map(int,input().split())
li=list(map(int,input().split()))

max_a=sum(li)

dp=[[ 0 for _ in range(n+1)]for _ in range(max_a+1)]
dp[max_a][n]=1

for j in range(n):
  for i in range(max_a+1):
    for k in range(n+1):
      if dp[i][k]>0:
        dp[i-li[j]][k-1]+=dp[i][k]
        
  
ans=0
for f in range(max_a+1):
  for g in range(n+1):
    if f==g*a:
      ans+=dp[f][g]
      
      
print(ans-1)