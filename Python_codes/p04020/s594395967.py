def solve():
  ans = 0
  N = int(input())
  A = [int(input()) for _ in range(N)]
  rem = 0
  for i in range(N):
    ans += (A[i]+rem)//2
    if A[i]>0:
      rem = (A[i]+rem)%2
    else:
      rem = 0
  return ans
print(solve())