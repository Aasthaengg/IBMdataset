n, a = map(int,input().split( ))

x = list(map(int,input().split( )))

for i in range(n):
    x[i] -= a

mx = 0
for i in range(n):
    mx += abs(x[i])
mx +=1

dp = [[0 for i in range(3*mx)] for j in range(n)]
dp[0][0] += 1
dp[0][x[0]] += 1

for i in range(1,n) :
    for j in range(-mx,mx):
        dp[i][j] += dp[i-1][j-x[i]]
        dp[i][j] += dp[i-1][j]
    #print(*dp[i])
print(dp[n-1][0]-1)
