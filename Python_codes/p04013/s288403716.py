n,a=map(int,input().split())
x=list(map(int,input().split()))
dp=[[[0]*(2501) for i in range(51)] for j in range(51)]
#dp[i][j][k]は、i番目まででj枚とって総数kとなる取り方
for i in range(n+1):
    dp[i][0][0]=1
for i in range(n):
    for j in range(1,i+2):
        for k in range(1,2501):
            if k-x[i]>=0:
                dp[i+1][j][k]=dp[i][j-1][k-x[i]]+dp[i][j][k]
            else:
                dp[i+1][j][k] = dp[i][j][k]
ans=0
for j in range(1,n+1):
    ans+=dp[n][j][a*j]
print(ans)