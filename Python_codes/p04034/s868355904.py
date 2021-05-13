n,m=map(int,input().split())
ans=[False]*n
ans[0]=True
co=[1]*n
for i in range(m):
  x,y=map(int,input().split())
  ans[y-1]|=ans[x-1]
  co[x-1]-=1
  co[y-1]+=1
  if co[x-1]==0:ans[x-1]=False
print(ans.count(True))