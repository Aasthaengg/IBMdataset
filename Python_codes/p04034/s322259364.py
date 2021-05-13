n,m=map(int,input().split())
flg=[False for i in range(n)]
flg[0]=True
t=[1 for i in range(n)]
tmp=1
for i in range(m):
    x,y=map(int,input().split())
    x,y=x-1,y-1
    t[x]-=1
    t[y]+=1
    if flg[x]:
        flg[y]=True
        if t[x]==1 and len(flg)==1:
            flg[x]=False

    if t[x]==0:
        flg[x]=False
ans=0
for i in range(n):
    if flg[i]:
        ans+=1
print(ans)