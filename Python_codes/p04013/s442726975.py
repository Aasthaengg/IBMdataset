n,A = map(int,input().split())
a = list(map(int,input().split()))
a = [x-A for x in a]
B = A*n
dp = [[0]*B*2 for i in range(n+1)]
dp[0][B] = 1
for i in range(n):
    for j in range(B*2):
        dp[i+1][j] += dp[i][j]
        k = j+a[i]
        if k >=0 and k<B*2:
            dp[i+1][k] += dp[i][j]
print(dp[n][B]-1)