n, a = [int(i) for i in input().split()]

x = [int(i) for i in input().split()] 
y = [int(i)-a for i in x] 


max = max(x)

dp = [[0 for _ in range(2*n*max+1)] for _ in range(n+1)]

dp[0][n*max] = 1 

for i in range(1, n+1):
	for j in range(2*n*max+1):
		if j - y[i-1] < 0 or j - y[i-1] > 2*n*max:
			dp[i][j] = dp[i-1][j]
		else: 
			dp[i][j] = dp[i-1][j] + dp[i-1][j-y[i-1]]

result = dp[n][n*max]-1

print(result)





