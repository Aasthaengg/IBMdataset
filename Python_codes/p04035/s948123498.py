n,l = [int(x) for x in input().split()]
x = [int(x) for x in input().split()]
c = -1
for i in range(n-1):
  if x[i] + x[i+1] >= l:
    c = i
    break

if c == -1:
  print("Impossible")
else:
  print("Possible")
  for i in range(1,c+1):
    print(i)
  for i in range(1,n - c):
    print(n - i)