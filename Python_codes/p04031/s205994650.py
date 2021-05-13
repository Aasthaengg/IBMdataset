n = int(input())
a = list(map(int, input().split()))

ans = 10000000
for i in range(-100, 101):
  sm = 0
  for x in a:
    sm += (x-i) ** 2
  ans = min(ans, sm)
  
print(ans)
