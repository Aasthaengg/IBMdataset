n,a = map(int,input().split())
xx = list(map(int,input().split()))

sm = sum(xx)
dp = [[0 for j in range(sm+1)] for i in range(n+1)]
dp[0][0] = 1
for x in xx:
    for i in range(1,n+1)[::-1]:
        for j in range(x,sm+1)[::-1]:
            # if dp[i-1][j-x]:
            dp[i][j] += dp[i-1][j-x]

ans = 0
for i in range(1, min(sm // a,n) + 1):
    ans += dp[i][i*a]
print(ans)
