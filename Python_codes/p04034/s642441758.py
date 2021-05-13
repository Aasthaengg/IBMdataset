n,m=map(int, input().split())
ball=[1]*n
red=[False]*n
red[0]=True
for i in range(m):
    x, y=map(int, input().split())
    x-=1
    y-=1
    ball[x]-=1
    ball[y]+=1
    if red[x]:
        red[y]=True
        if ball[x]==0:
            red[x]=False

print(red.count(True))