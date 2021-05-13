import sys
input = sys.stdin.readline

N, A = [int(x) for x in input().split()]
x = [int(x) - A for x in input().split()]

dp = [[0] * 5001 for _ in range(N + 1)]
dp[0][0 + 2500] = 1

for i in range(1, N + 1):
    for j in range(-2500, 2501):
        if 5000 >= j + 2500 - x[i - 1] >= 0:
            dp[i][j + 2500] = dp[i - 1][j + 2500 - x[i - 1]] + dp[i - 1][j + 2500]
        else:
            dp[i][j + 2500] = dp[i - 1][j + 2500]

print(dp[N][0 + 2500] - 1) # 何も選ばないものを引く