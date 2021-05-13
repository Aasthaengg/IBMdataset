n,a=map(int,input().split())

x=list(map(int,input().split()))
A=max(x)
x.insert(0,-1)
dp=[[[0]*(n+1) for _ in range(n*A+1)] for i in range(n+1)]
dp[1][x[1]][1]=1
dp[1][0][0]=1
for i in range(1,n):
    q=x[i+1]
    for s in range(n*A+1):
        for k in range(i+1):
            if s+q<=n*A:
                dp[i+1][s+q][k+1]+=dp[i][s][k]
            dp[i+1][s][k]+=dp[i][s][k]

ans=0
i=1

while i<=n and a*i<=n*A:
    ans+=dp[n][a*(i)][i]
    i+=1
print(ans)


