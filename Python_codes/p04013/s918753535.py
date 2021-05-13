
N, M = map(int, input().split())
D = list(map(int, input().split()))
dp = [[0] * 2551 for i in range(51)]
dp[0][0] = 1
for k in D:
    for i in range(49, -1, -1):
        for j in range(2500, -1, -1):
            dp[i+1][j + k] += dp[i][j]

ans = 0
for i in range(1, N+1):
    ans += dp[i][i*M]
print(ans)



