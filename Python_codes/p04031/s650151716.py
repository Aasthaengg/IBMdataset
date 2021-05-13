n=int(input())
a=list(map(int,input().split()))
ans=1000000

for i in range(-100,101):
  cou=0
  for j in range(n):
    cou+=(a[j]-i)**2
  ans=min(ans,cou)
  
print(ans)