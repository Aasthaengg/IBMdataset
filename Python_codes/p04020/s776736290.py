n,*a = map(int,open(0).read().split())
ans = a[0]//2
a[0] %= 2
for i in range(n-1):
  if a[i] == 1 and a[i+1] != 0:
    ans += 1
    a[i+1] -= 1
  if a[i+1] >1:
    ans += a[i+1]//2
    a[i+1] %= 2
print(ans)