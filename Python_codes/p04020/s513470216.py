n,*a=map(int,open(0).read().split())
ans=0
if n==1:
  print(a[0]//2)
  exit()
for i in range(n-1):
  if (a[i]+a[i+1])%2==0:
    ans+=(a[i]+a[i+1])//2
    a[i+1]=0
  else:
    ans+=(a[i]+a[i+1])//2
    a[i+1]=(0 if a[i+1]==0 else 1)
print(ans)