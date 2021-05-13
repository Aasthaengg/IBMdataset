n,a=map(int,input().split())
x=list(map(int,input().split()))

xsum=max(max(x),a)*n
dp=[[[0]*(xsum+1) for i in range(n+1)] for ii in range(n+1)]

dp[0][0][0]=1

for j in range(1,n+1):
    for k in range(0,n+1):    
        for s in range(0,xsum+1):    
            if s<x[j-1] :
                dp[j][k][s]=dp[j-1][k][s]
            elif s>=x[j-1] and k>=1:
                dp[j][k][s]=dp[j-1][k][s]+dp[j-1][k-1][s-x[j-1]]
            else:
                dp[j][k][s]=0
dsum=0
for k in range(1,n+1):
    dsum=dsum+dp[n][k][k*a]
print(dsum)
    
