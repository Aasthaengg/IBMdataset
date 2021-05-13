N, A = map(int, input().split())
x = list(map(int, input().split()))
MAX_J = sum(x)
dp = [[0] * (MAX_J+1) for i in range(N+1)]
dp[0][0] = 1
for n in range(N):
    for i in range(N)[::-1]:
        for j in range(MAX_J-x[n]+1)[::-1]:
            dp[i+1][j+x[n]] += dp[i][j]
ans = 0
for i in range(1, N+1):
    if A * i <= MAX_J:
        ans += dp[i][A * i]
print(ans)
