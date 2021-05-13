N = int(input())
A = [0] + [int(input()) for i in range(N)]

ans = 0
for i in range(1, N+1):
  a = A[i]; pre_a = A[i-1]
  if pre_a == 1 and a >= 1:
    ans += 1
    a -= 1
  ans += a//2
  A[i] = a % 2

print(ans)