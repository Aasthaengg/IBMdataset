n,m=map(int,input().split())
check=[False]*n
check[0]=True
ball=[1]*n
for i in range(m):
    x,y=map(int,input().split())
    x-=1
    y-=1
    if check[x]:
        check[y]=True

    ball[y]+=1
    ball[x]-=1
    if ball[x]==0:
        check[x]=False

ans=0

for chk in check:
    if chk:
        ans+=1

print(ans)

