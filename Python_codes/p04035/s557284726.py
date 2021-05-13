def dump(n,k):
  for i in range(k-1):
    print(i+1)
  for i in range(n-1,k-1,-1):
    print(i)

n,l=map(int,input().split(' '))
a=input().split(' ')
a=[int(s) for s in a]

k=0
for i in range(n-1):
  if a[i]+a[i+1]>=l:
    k=i+1
    break

if k==0:
  print("Impossible")
else:
  print("Possible")
  dump(n,k)
