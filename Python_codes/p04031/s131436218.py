n = int(input())
a = list(map(int, input().split()))

m = round(sum(a)/n)
ans = 0
for i in a:
  ans += (i-m)**2
print(ans)