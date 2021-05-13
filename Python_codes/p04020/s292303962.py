N = int(input())
A = [int(input()) for _ in range(N)]
ans = 0
for i in range(N-1):
  dup1 = A[i] // 2
  A[i] -= dup1 * 2
  dup2 = min(A[i], A[i+1])
  A[i+1] -= dup2
  ans += dup1 + dup2
dup1 = A[-1] // 2
ans += dup1
print(ans)