from itertools import accumulate as ac

n,l=map(int,input().split())
*a,=map(int,input().split())
v=[]

for i in range(n-1):
  if a[i]+a[i+1]>=l:
    v.append(i+1)
    break
else:
  print("Impossible")

if v:
  st=v[0]
  v+=list(range(1,st)[::-1])
  v+=list(range(st+1,n))
  print("Possible")
  for i in v[::-1]:
    print(i)