import sys
n, l = map(int, input().split())
a = [int(x) for x in input().split()]

key = -1
for i in range(n-1):
  if a[i]+a[i+1] >= l:
    key = i
    break

if key == -1:
  print("Impossible")
else:
  print("Possible")
  for i in range(key):
    print(i+1)
  for i in range(n-1, key, -1):
    print(i)