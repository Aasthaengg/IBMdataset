n = int(input())
a = list(map(int, input().split()))

m = sum(a)//n
ans = float("inf")
for i in range(m, m+2):
  t = 0
  for j in a:
    t += abs(j-i)**2
  ans = min(t,ans)
print(ans)