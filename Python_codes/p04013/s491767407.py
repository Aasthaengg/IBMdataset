N, A = map(int, input().split())  # N枚数のカード, 平均をAにしたい
X = tuple(map(int, input().split()))  # N枚のカードの中身

dp = [[[0]*(50*N+2) for _ in range(N+2)] for _ in range(N+2)]

dp[0][0][0] = 1  # 0枚の中から0枚選んで合計が0になる選び方が1通りある

for i in range(N):
    for j in range(N+1):
        for k in range(50*N+1):
            # if dp[i][j][k]:  # ここの分岐が分からん
            if k+X[i] < 50*N+2:
                dp[i+1][j][k] += dp[i][j][k]
                dp[i+1][j+1][k+X[i]] += dp[i][j][k]
ans = 0
for i in range(1, N+1):
    ans += dp[N][i][i*A]
print(ans)
