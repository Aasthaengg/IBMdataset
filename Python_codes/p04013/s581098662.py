# DP

# https://atcoder.jp/contests/abc044/tasks/arc060_a

from itertools import combinations


n, a = map(int, input().split())
x = list(map(int, input().split()))
X = max(max(x), a)


# dp[j][k][s] (0 <= j <= N, 0 <= k <= N, 0 <= s <= NX)
# dp[j][k][s] = x1,...,xjまでからk枚使って，合計をsにする選び方の総数
# dp[0][0][0] = 1
# j >= 1, s < xjのとき，dp[j][k][s] = dp[j-1][k][s] (xjは使わない)
# j >= 1, k >= 1, s >= xjのとき，dp[j][k][s] = dp[j-1][k][s] + dp[j-1][k-1][s-xj]
# ... 1枚少なく使ってxjを入れる + 使わない
# それ以外 0

dp = [
    [[0 for _ in range(n * X + 1)] for _ in range(n + 2)]
    for _ in range(n + 2)
]

dp[0][0][0] = 1
for i in range(n):
    for j in range(n+1):
        for k in range(n * X + 1):
            if k < x[i]:
                dp[i + 1][j][k] = dp[i][j][k]
            else:
                dp[i + 1][j][k] = dp[i][j][k] + dp[i][j-1][k-x[i]]
ans = 0
for i in range(1, n + 1):
    ans += dp[n][i][i*a]
print(ans)