n,*x=map(int,open(0).read().split())
y=[x[0]-i for i in x]
m=n*max(x)
dp=[[0]*(m*2+1) for _ in range(n+1)]
dp[0][0]=1
for i in range(1,n+1):
	for s in range(-m,m):
		dp[i][s]=dp[i-1][s]+dp[i-1][s-y[i]]
print(dp[n][0]-1)