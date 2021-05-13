n = int(input())
a = list(map(int, input().split()))

b = min(a)
c = max(a)
ans = []
for i in range(b, c+1):
  res = 0
  for j in a:
    res += (j - i)**2
  ans.append(res)

print(min(ans))