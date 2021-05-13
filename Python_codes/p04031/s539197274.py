import math
N = int(input())
a = list(map(int, input().split()))
a.sort()

ans = math.inf
for i in range(a[0], a[-1]+1):
  tmp = 0
  for j in range(N):
    tmp += (a[j]-i) ** 2
  if ans >= tmp:
    ans = tmp
  else:
    break
print(ans)