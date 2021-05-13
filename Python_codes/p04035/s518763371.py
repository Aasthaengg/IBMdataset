n,l=map(int,input().split())
a=list(map(int,input().split()))
if a[0]+a[1]>=l:
  print("Possible")
  for i in range(n-1,0,-1):print(i)
  exit()
if a[-2]+a[-1]>=l:
  print("Possible")
  for i in range(1,n):print(i)
  exit()
ans=-1
for i in range(1,n):
  if a[i-1]+a[i]>=l:
    ans=i
    break
if ans==-1:print("Impossible")
else:
  print("Possible")
  for i in range(1,ans):print(i)
  for i in range(n-1,ans,-1):print(i)
  print(ans)
