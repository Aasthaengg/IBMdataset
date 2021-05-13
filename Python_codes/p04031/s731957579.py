N = int(input())
a = list(map(int, input().split()))
a = sorted(a)

x = sum(a)
if x > 0:
  x = int(x/N+0.5)
else:
  x = int(x/N-0.5)

total = 0
if a[0] == x and a[-1] == x:
  print(0)
else:  
  for i in range(N):
    total += (x-a[i])**2
  print(int(total))