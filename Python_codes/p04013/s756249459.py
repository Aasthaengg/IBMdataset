N,A = [int(x) for x in input().split()]
x = [int(x) for x in input().split()]
X = max(x+[A])
#%%
dp = [[[-1]*(N*X+1) for _ in range(N+1)] for _ in range(N+1)]

def rep(j,k,s):
    if(dp[j][k][s]==-1):
        if(s==j==k==0):
            dp[j][k][s] = 1
        elif(j>=1 and s<x[j-1]):
            dp[j][k][s] = rep(j-1,k,s)
        elif(j>=1 and k>=1 and s>=x[j-1]):
            dp[j][k][s] = rep(j-1,k,s) + rep(j-1,k-1,s-x[j-1])
        else:
            dp[j][k][s] = 0
    return dp[j][k][s]

ans = 0
for k in range(1,N+1):
    ans += rep(N,k,k*A)
print(ans)
