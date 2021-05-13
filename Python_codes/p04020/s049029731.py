from copy import copy
n=int(input())
a=[0]+[int(input()) for _ in range(n)]
ans=0
for i in range(n):
  ans+=(a[i+1]+a[i])//2
  if a[i+1]:a[i+1]=(a[i+1]+a[i])%2
print(ans)