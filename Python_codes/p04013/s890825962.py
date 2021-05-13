n , a= map(int , input().split())
arr = list(map(int , input().split()))
dp = [ [[ 0 for j in range(0 , a*(n+2))] for k in range(0 , n+2)] for i in range(0,n+2)]
dp[0][0][0]=1
b=[0 for i in range(0 , n+1)]
for i in range(0 , n):
	b[i+1]=arr[i]
for i in range(1 , n+1):	# choosing only first i elements
	for j in range(0 , i+1):# choosing only j elements from first i elements
		for k in range(0 , a*(n)+2):# no of ways of forming a sum k taking j elements out of i elements
			if k<b[i]:
				dp[i][j][k]=dp[i-1][j][k]
			else:
				dp[i][j][k]=dp[i-1][j][k]+dp[i-1][j-1][k-b[i]]
tot = 0
for i in range(1 , n+1):
	tot = tot + dp[n][i][(i)*a]
print(tot)