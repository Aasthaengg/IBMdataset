N, A = list(map(int, input().split()))
x = list(map(int, input().split()))
X = max(max(x), A)

dp=[[[0 for k in range(N*X+1)] for j in range(N+1)] for i in range(N+1)]

ans = 0
for j in range(N+1):
  for k in range(N+1):
    for s in range(N*X+1):
      if j==0 and k==0 and s==0:
        dp[j][k][s]=1
      elif j>=1 and s<x[j-1]:
        dp[j][k][s] = dp[j-1][k][s]
      elif j>=1 and k>=1 and s>=x[j-1]:
        dp[j][k][s] = dp[j-1][k][s] + dp[j-1][k-1][s-x[j-1]]
      else:
        dp[j][k][s] = 0
      if j==N and s==k*A:
        ans = ans + dp[j][k][s]
print(ans-1)
