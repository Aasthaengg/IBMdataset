N,A=map(int, input().split())
X=list(map(int, input().split()))
dp=[[[0]*(2501) for _ in range(N+1)]for _ in range(N+1)]
dp[0][0][0]=1
#dp[i][j][k]i枚目を検討中、j枚選び、合計kとなるのは何通りか
for i in range(N):
  for j in range(N+1):
    for k in range(2501):
      if not dp[i][j][k]:
        continue
      dp[i+1][j][k]+=dp[i][j][k]
      if j<N:
        dp[i+1][j+1][k+X[i]]+=dp[i][j][k]
ans=0
for i in range(1,N+1):
  ans+=dp[N][i][i*A]
print(ans)