N, A = map(int, input().split())
x = list(map(int, input().split()))

#dp[j][k][s] = (x0...xj からk枚選んでxiの合計をsにするような選び方の総数)
dp = [[[0] * (A * N + 1) for k in range(N + 1)] for j in range(N)]

dp[0][0][0] = 1
if x[0] <= A * N:
    dp[0][1][x[0]] = 1

for j in range(N - 1):
    for k in range(N + 1):
        for s in range(A * N + 1):
            if k == 0 and s == 0:
                dp[j + 1][k][s] = 1
            elif k > j + 2:
                dp[j + 1][k][s] = 0
            elif s >= x[j + 1] and k >= 1:
                dp[j + 1][k][s] = dp[j][k][s] + dp[j][k - 1][s - x[j + 1]]
            else:
                dp[j + 1][k][s] = dp[j][k][s]

res = 0
for i in range(1, N + 1):
    res += dp[N - 1][i][A * i]

print(res)