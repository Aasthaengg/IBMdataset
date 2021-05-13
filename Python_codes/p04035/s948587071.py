n,l=map(int,input().split())
a=list(map(int,input().split()))
last=-1
for i in range(n-1):
  if a[i]+a[i+1]>=l:
    last=i+1
if last==-1:
  print("Impossible")
else:
  print("Possible")
  for i in range(1,last):
    print(i)
  for i in range(len(a)-1,last-1,-1):
    print(i)
