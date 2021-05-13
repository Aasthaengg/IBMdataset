import sys
input=sys.stdin.readline
n,a=map(int,input().split())
x=[0]+list(map(int,input().split()))
su=sum(x)
maxi=max(x)
dp=[[[0 for k in range(maxi*n+1)] for j in range(51)] for i in range(51)]
dp[0][0][0]=1
for i in range(1,n+1):
    for j in range(i+1):
        for k in range(maxi*j+1):
            if k<x[i]:
                dp[i][j][k]=dp[i-1][j][k]
            if k>=x[i] and j>=1:
                dp[i][j][k]=dp[i-1][j][k]+dp[i-1][j-1][k-x[i]]
ans=0
for t in range(1,n+1):
    if a*t<=su:
        ans+=dp[n][t][a*t]
    else:
        break
print(ans)
