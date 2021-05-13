n,a = list(map(int,input().split()))
x = list(map(int,input().split()))

def Count(n,k,a):
	s = sum(x)
	dp=[[[0 for l in range(s+1)] for j in range(k+1)] for i in range(n+1)]
	dp[0][0][0]=1
	Sum=0
	for i in range(n):
		for j in range(k+1):
			for l in range(s+1):
				if l < x[i]:
					dp[i+1][j][l] = dp[i][j][l]
				if j >=1 and l >= x[i]:
					dp[i+1][j][l] = dp[i][j][l] + dp[i][j-1][l-x[i]]
				if j <= i+1 and l ==j*a and j >= 1:
					if dp[i+1][j][l]>=1:	
						Sum += dp[i+1][j][l]-dp[i][j][l]
	return Sum

print(Count(n,n,a))

