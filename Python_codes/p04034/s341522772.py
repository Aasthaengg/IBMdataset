n,m=map(int,input().split())
red=[1]+[0]*(n-1)
pink=[1]*n
for _ in range(m):
    x,y=map(int,input().split())
    x-=1
    y-=1
    if red[x] and pink[x]==1:
        red[x]=0
        red[y]=1
    elif red[x] and pink[x]>1:
        red[y]=1
    pink[x]-=1
    pink[y]+=1
print(red.count(1))