n=int(input())

a=[]

for i in range(n):
  a.append(int(input()))

ans=0
for i in range(n-1):
  ans+=a[i]//2
  a[i]=a[i]%2
  if a[i]==1 and a[i+1]>=1:
    ans+=1
    a[i]-=1
    a[i+1]-=1
ans+=a[n-1]//2

print(ans)