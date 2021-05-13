n,a=map(int,input().split())
x=list(map(int,input().split()))
# dp[j][k][s]=(x1,...,xjからk枚選んでx[i]の合計をsにするような選び方の総数)
dp=[[[0]*2501 for i in range(51)] for j in range(51)]
dp[0][0][0]=1
for i in range(n):
    for j in range(n+1):
        for k in range(2501):
            if k<x[i]:
                dp[i+1][j][k]=dp[i][j][k]
            else:
                dp[i+1][j][k]=dp[i][j][k]+dp[i][j-1][k-x[i]]
ans=0
for i in range(1,n+1):
    ans+=dp[n][i][i*a]
print(ans)