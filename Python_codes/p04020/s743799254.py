def solve():
  N = int(input())
  A = [int(input()) for _ in range(N)]
  ans = A[0]//2
  A[0] = A[0]%2
  for i in range(1,N):
    ans += (A[i]+A[i-1])//2
    if (A[i]+A[i-1])//2>0:
      A[i] = (A[i]+A[i-1])%2
  return ans
print(solve())