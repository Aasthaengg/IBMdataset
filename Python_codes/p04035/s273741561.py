n,l = map(int,input().split())
a = [int(i) for i in input().split()]
for i in range(n-1):
  if a[i]+a[i+1] >= l:
    print('Possible')
    for j in range(n-1,i+1,-1):
      print(j)
    for k in range(1,i+2):
      print(k)
    exit()
print('Impossible')