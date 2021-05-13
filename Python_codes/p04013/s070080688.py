n,x=map(int,input().split())
l=[int(i) for i in input().split()]
dp = [[[0 for k in range(55)] for j in range(3000)] for i in range(55)]

for i in range(n+1):
    dp[i][0][0]=1 
sm=sum(l)
for i in range(1,n+1):
    for j in range(sm+5):
        for k in range(1,n+1):
            curr=l[i-1]
            if curr<=j:
                dp[i][j][k]=dp[i-1][j][k]+dp[i-1][j-curr][k-1]
            else:
                dp[i][j][k]=dp[i-1][j][k]

ans=0 
for k in range(1,n+1):
    ans+=dp[n][k*x][k]
print(ans)