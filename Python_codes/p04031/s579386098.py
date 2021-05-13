n = int(input())
a = list(map(int, input().split()))

ans = float("inf")
for y in range(-100, 101):
  res = 0
  for x in a:
    res += (x - y)**2
  ans = min(ans, res)

print(ans)
