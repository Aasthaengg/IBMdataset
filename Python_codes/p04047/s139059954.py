N = int(input())
L = sorted([int(i) for i in input().strip().split()])
ans = 0
for n in range(N):
  ans += min(L[2*n], L[2*n+1])
print(ans)