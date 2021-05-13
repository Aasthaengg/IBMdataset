n,m=map(int,input().split())
num=[1]*n
aka=[0]*n
aka[0]=1
for _ in range(m):
  x,y=map(int,input().split())
  if num[x-1]>1 and aka[x-1]==1:
    num[x-1]+=-1
    aka[x-1]=1
    aka[y-1]=1
    num[y-1]+=1
  elif num[x-1]==1 and aka[x-1]==1:
    num[x-1]=0
    aka[x-1]=0
    aka[y-1]=1
    num[y-1]+=1
  elif aka[x-1]==0:
    num[x-1]+=-1
    num[y-1]+=1
print(sum(aka))
