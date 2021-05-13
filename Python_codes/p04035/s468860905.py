import numpy as np
n,l=map(int,input().split())
a=list(map(int,input().split()))
flag=False;idx=0
for i in range(n-1):
  if a[i]+a[i+1]>=l:
    flag=True
    idx=i
if not flag:
  print("Impossible")
  exit(0)
print("Possible")
for x in range(idx):
  print(x+1)
for x in reversed(range(idx,n-1)):
  print(x+1)
