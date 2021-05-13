n,m=map(int,input().split())
ans=[0]*n
ans[0]=1
b=[1]*n
for i in range(m):
  x,y=map(int,input().split())
  if ans[x-1]==1 and b[x-1]>1:
    ans[y-1]=1
    b[x-1]=b[x-1]-1
    b[y-1]=b[y-1]+1
  elif ans[x-1]==1 and b[x-1]==1:
    ans[x-1]=0
    ans[y-1]=1
    b[x-1]=b[x-1]-1
    b[y-1]=b[y-1]+1
  else:
    b[x-1]=b[x-1]-1
    b[y-1]=b[y-1]+1
print(sum(ans))