n = int(input())
a = [int(input()) for i in range(n)]

c = 0

for i in range(n-1):
  if a[i]%2 == 1 and a[i+1]>=1:
    c += 1
    a[i] -= 1
    a[i+1] -= 1
for i in range(n):
  c += a[i]//2
  a[i] -= (a[i]//2)*2
print (c)