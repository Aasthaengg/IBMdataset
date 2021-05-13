N, A = map(int, input().split())
nums = list(map(int, input().split()))
MAX = A*N
dp = [[0 for _ in range(A*N+1)] for _ in range(N+1)]
dp[0][0] = 1
for k, num in enumerate(nums, start=1):
  for i in range(N-1, -1, -1):
    for j in range(A*N-1, -1, -1):
      if j + num <= A*N:
        dp[i+1][j+num] += dp[i][j]
ans = 0
for i in range(1, N+1):
  ans += dp[i][i*A]
print(ans)