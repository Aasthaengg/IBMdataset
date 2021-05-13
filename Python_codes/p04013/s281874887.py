n,a=map(int,input().split())
x=list(map(int,input().split()))

xmax=max(max(x),a)
    
nx=n*xmax
dp=[[[0]*(nx+1) for ii in range(n+1)] for i in range(n+1)]

dp[0][0][0]=1

for j in range(1,n+1):
    jj=j-1
    for k in range(n+1):
        for s in range(nx+1):
            if s<x[jj]:
                dp[j][k][s]=dp[j-1][k][s]
            elif 1<=k and  x[jj]<=s:
                dp[j][k][s]=dp[j-1][k][s]+dp[j-1][k-1][s-x[jj]]
            else:
                dp[j][k][s]=0
#            if dp[j][k][s]!=0:
#                print(j,k,s,dp[j][k][s])
dpsum=0
for k in range(1,n+1):
    dpsum=dpsum+dp[n][k][k*a]
                
print(dpsum)
        
