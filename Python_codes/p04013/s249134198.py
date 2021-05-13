N, A = map(int, input().split())
X = list(map(int, input().split()))
xmax = max(X)

OFS = N*xmax
dp = [[0]*(2*OFS+1) for _ in range(N)]
dp[0][OFS] += 1
dp[0][OFS+(X[0]-A)] += 1

for i in range(1, N):
  for s in range(2*OFS+1):
    t = s-(X[i]-A)
    if t < 0 or t > 2*OFS:
      dp[i][s] = dp[i-1][s]
    else:
      dp[i][s] = dp[i-1][s] + dp[i-1][t]

      
print(dp[N-1][OFS]-1)