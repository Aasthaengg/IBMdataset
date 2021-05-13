n,m = map(int,input().split())
x_li = [0]*m
y_li = [0]*m
for i in range(m):
    x_li[i],y_li[i]=map(int,input().split())

map_li = [1]*n
red = [False]*n
red[0]=True

for i in range(m):
    x,y = x_li[i],y_li[i]
    x,y = x-1,y-1
    if red[x] and map_li[x]>1:
        red[y]=True
    elif red[x]:
        red[y]=True
        red[x]=False
    map_li[x]-=1
    map_li[y]+=1
#print(map_li)
print(sum(red))