# C - 高橋君とカード
n,a=map(int,input().split())
x=list(map(int,input().split()))

max_num=max(n*a,sum(x))
dp=[[[0]*(max_num+1) for j in range(n+1)] for i in range(n+1)]
dp[0][0][0]=1
for i in range(n):
    for j in range(n):
        for k in range(max_num):
            if dp[i][j][k]:
                # not use
                dp[i+1][j][k] += dp[i][j][k]
                #  use
                dp[i+1][j+1][k+x[i]] += dp[i][j][k]

ans=0
for i in range(1,n+1):
    ans+=dp[n][i][i*a]
print(ans)