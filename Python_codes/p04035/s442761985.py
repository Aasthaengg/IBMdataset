N, L = map(int, input().split())
a = [int(c) for c in input().split()]
m = 10**9
j = -1
for i in range(N-1):
  if a[i]+a[i+1]>=L:
    print('Possible')
    for j in range(1,i+1):
      print(j)
    for j in range(N-1, i+1, -1):
      print(j)
    print(i+1)
    break
else:
  print('Impossible')
