n,a = map(int,input().split())
x = sorted(list(map(lambda y:int(y)-a,input().split())))

sx = max(abs(x[0]),abs(x[-1]))*n

dp = [[0 for _ in range(2*sx+2)] for _ in range(n+1)]
dp[0][0] = 1

for j in range(n):
    for t in range(-sx-1,sx+1):
        if -sx <= t-x[j] and t-x[j] <= sx: 
            dp[j+1][t] = dp[j][t] + dp[j][t-x[j]]
        else:
            dp[j+1][t] = dp[j][t]

print(dp[n][0]-1)