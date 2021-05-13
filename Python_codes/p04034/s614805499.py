n,m=map(int,input().split())
a=[1]*(n+1)
b=[0]*(n+1)
b[1]=1
for _ in range(m):
  x,y=map(int,input().split())
  a[x]-=1
  a[y]+=1
  if b[x]:b[y]=1
  if a[x]==0:b[x]=0
print(sum(b))