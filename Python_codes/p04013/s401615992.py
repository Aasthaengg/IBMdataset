n, a = map(int, input().split())
x = list(map(int, input().split()))
sum_x = sum(x)
sum_x = max(sum_x, n*a)

dp = [[[0]*(sum_x+1) for _ in range(n+1)] for _ in range(n+1)]
#dp[i][j][k]はi番目までのカードの中からj枚選んで、合計がkになるときの選び方の総数
dp[0][0][0] = 1

for i in range(n):
    for j in range(n):
        for k in range(sum_x+1):
            if k-x[i] >= 0:
                dp[i+1][j+1][k] += dp[i][j][k-x[i]]
            dp[i+1][j][k] += dp[i][j][k]

ans = 0
for i in range(1, n+1):
    ans += dp[n][i][i*a]
    #print(dp[n][i][i*a])
print(ans)

