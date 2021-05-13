n,m=map(int,input().split())
numl=[1]*n
l=[False]*n
l[0]=True
for i in range(m):
    x,y=map(int,input().split())
    x-=1
    y-=1
    numl[x]-=1
    numl[y]+=1
    if l[x]:
        l[y]=True
        if numl[x]==0:
            l[x]=False
print(l.count(True))