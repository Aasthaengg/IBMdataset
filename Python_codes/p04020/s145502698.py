N = int(input())
A = [int(input()) for _ in range(N)]
ans = 0
if 0 not in A:
  ans = sum(A)//2
else:
  now = 0
  for i in range(N):
    if A[i] == 0 or i == N-1:
      ans += sum(A[now:i+1])//2
      now = i+1
print(ans)