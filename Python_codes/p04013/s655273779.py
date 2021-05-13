n, a = map(int,input().split())
x = list(map(int,input().split()))

dp = [[[0] * n for i in range(n * a + 1)] for i in range(n)]
for i in range(n):
    for j in range(n * a + 1):
        for k in range(n):
            if i == 0 and x[0] < n * a + 1:
                dp[0][x[0]][0] = 1
                break
            else:
                if j == 0:
                    if k == 0 and x[i] < n * a + 1:
                        dp[i][x[i]][0] += 1
                    continue

                if dp[i - 1][j][k] == 0:continue
                dp[i][j][k] += dp[i - 1][j][k]
                if not(0 <= j + x[i] < n * a + 1):continue
                dp[i][j + x[i]][k + 1] += dp[i - 1][j][k]
cnt = 0
for i in range(n * a + 1):
    if i != 0 and i % a == 0:
        temp = i // a
        cnt += dp[-1][i][temp - 1]
print(cnt)
