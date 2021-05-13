import sys
readline = sys.stdin.readline

N = int(readline())
A = [int(readline()) for i in range(N)]

ans = 0
for i in range(N):
  pair, mod = divmod(A[i],2)
  ans += pair
  if mod:
    if i + 1 < N and A[i + 1] > 0:
      ans += 1
      A[i + 1] -= 1
  
print(ans)
