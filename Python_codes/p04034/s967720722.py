n,m=map(int,input().split())
data=[1]*n
d=[1]+[0]*(n-1)
for i in range(m):
  x,y=map(int,input().split())
  data[x-1]-=1
  data[y-1]+=1
  if d[x-1]==1:
    d[y-1]=1
  if data[x-1]==0:
    d[x-1]=0
print(d.count(1))