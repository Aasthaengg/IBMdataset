n, a = map(int, input().split())
x = [0] + list(map(int, input().split()))
nx = 2501

# DP: x1からxjまでの間でk枚を選んで合計がsになる組み合わせの数
dp = [ [ [0 for s in range(nx+1)] for k in range(n+1)] for j in range(n+1)]
dp[0][0][0] = 1

for j in range(1, n+1):
    for k in range(n+1):
        for s in range(nx+1):
            if x[j] > s:
                dp[j][k][s] = dp[j-1][k][s]
            elif k >= 1:
                dp[j][k][s] = dp[j-1][k][s] + dp[j-1][k-1][s-x[j]]
#print(dp)
ans = 0
for k in range(1, n+1):
    ans += dp[-1][k][a * k]

print(ans)
