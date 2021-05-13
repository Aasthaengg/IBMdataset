N,A=map(int,input().split())
x=list(map(int,input().split()))
dp=[[[0]*2600 for j in range(N+10)] for i in range(N+10)]
dp[0][0][0]=1
for i in range(N):
    for j in range(N+1):
        for k in range(2501):
            if(dp[i][j][k]!=0):
                dp[i+1][j][k]+=dp[i][j][k]
                dp[i+1][j+1][k+x[i]]+=dp[i][j][k]
print(sum(dp[N][i][i*A] for i in range(1,N+1)))