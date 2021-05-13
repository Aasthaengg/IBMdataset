N, A = map(int, input().split())
# 予め-Kした状態で用意しておく
X = [A-int(x) for x in input().split()]
MAX = N*A*2
# dp[i][k] := i枚目までのカードで、合計をkにする通り数
dp = [[0]*(MAX+1) for _ in range(N+1)]
# 負の数を考慮して、N*K位置を0とする
dp[0][N*A] = 1
for i in range(N):
  x = X[i]
  for k in range(MAX+1):
    dp[i+1][k] += dp[i][k]
    if 0 <= k+x <= MAX:
      dp[i+1][k+x] += dp[i][k]
      
# N回終わって合計が0になっている通り数 - 1枚も取らないケース      
print(dp[N][N*A]-1)