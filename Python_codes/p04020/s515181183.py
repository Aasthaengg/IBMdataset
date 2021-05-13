N = int(input())
A = [int(input()) for _ in range(N)]

A.append(0)
ans = 0

for i in range(N):
  ans += A[i] // 2
  if A[i + 1] != 0:
    A[i + 1] += A[i] % 2

print(ans)