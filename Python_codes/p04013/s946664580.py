N,A = map(int,input().split())
x = list(map(int,input().split()))

temp = x + [A]

X = max(temp)

m = N * X

dp = [[[0 for s in range(m+1)] for k in range(N+1)] for j in range(N+1)]

dp[0][0][0] = 1

res = 0

for j in range(N):
    for k in range(N):
        for s in range(m):
            if dp[j][k][s]:
                dp[j+1][k][s] += dp[j][k][s]
                dp[j+1][k+1][s+x[j]] += dp[j][k][s]

for k in range(1,N+1):
    res += dp[N][k][k*A]

print(res)
