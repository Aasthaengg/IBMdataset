n = int(input())
a = tuple(map(int,input().split()))

ans = float('inf')
for x in range(-100,101,1):
  c = 0
  for ai in a:
    c += (x-ai)**2
  ans = min(c,ans)
print(ans)
