import sys
n,x=map(int,input().split())
a=list(map(int,input().split()))
k=-1
for i in range(n-1):
  if a[i]+a[i+1]>=x:
    k=i
    break
  if i==n-2:
    print('Impossible')
    sys.exit()
print('Possible')
for i in range(k):
  print(i+1)
for i in range(n-2,k,-1):
  print(i+1)
print(k+1)