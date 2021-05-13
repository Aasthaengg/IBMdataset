N=int(input())
a=list(map(int,input().split()))
ans=10**9
for i in range(-100,101):
  bns=0
  for j in range(N):
    bns+=(abs(a[j]-i)**2)
  ans=min(ans,bns)
print(ans)