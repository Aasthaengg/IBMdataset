N = int(input())
L = list(map(int, input().split()))
ans = 0

L = sorted(L)

for i in range(1,N+1):
  ans += (L[-i*2])

print(ans)