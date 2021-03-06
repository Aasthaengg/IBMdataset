n, a = map(int, input().split())
X = tuple(map(int, input().split()))
dp = [[[0] * (2550) for _ in range(n+1)] for _ in range(n+1)]
dp[0][0][0] = 1
for i in range(n):
    # i枚目までで
    for j in range(n):
        # j枚のカードを選んで
        for s in range(n*a+1):
            # 合計がsになるパターン
            if dp[i][j][s] == 0:
                continue
            # i枚目のカードが選ばれない場合
            dp[i+1][j][s] += dp[i][j][s]
            # i枚目のカードが選ばれる場合
            dp[i+1][j+1][s+X[i]] += dp[i][j][s]
ans = 0
for k in range(1, n+1):
    ans += dp[n][k][k*a]
print(ans)
