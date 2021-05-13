n,m=map(int,input().split())
xy=[]
for _ in range(m):
    x,y=map(int,input().split())
    xy.append([x,y])

ball=[1]*n
red=[0]*n
red[0]+=1

for i in range(m):
    if red[xy[i][0]-1]>=1:
        if ball[xy[i][0]-1]==1:
            red[xy[i][0]-1]=0
        red[xy[i][1]-1]+=1
    ball[xy[i][0]-1]-=1
    ball[xy[i][1]-1]+=1

ans=len(red)-red.count(0) 
print(ans)