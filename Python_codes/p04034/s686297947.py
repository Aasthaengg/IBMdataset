n,m=map(int, input().split())
xy=[list(map(int, input().split())) for _ in range(m)]

ball=[1]*n
red=[False]*n
red[0]=True
for i in range(m):
    x=xy[i][0]-1
    y=xy[i][1]-1
    if red[x]:
        red[y]=True
        if ball[x]==1:
            red[x]=False
    ball[y]+=1
    ball[x]-=1
print(red.count(True))
