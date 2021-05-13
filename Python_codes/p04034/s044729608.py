n,m=map(int,input().split())
x,y=[0]*m,[0]*m
res=[1]*n
red=[0 for i in range(n)]
red[0]=1
for i in range(m):
    x[i],y[i]=map(int,input().split())
    if red[x[i]-1]==0 and red[y[i]-1]==0:
        res[x[i]-1]-=1
        res[y[i]-1]+=1
    elif red[x[i]-1]>0 and red[y[i]-1]==0:
        res[x[i]-1]-=1
        red[x[i]-1]-=1
        res[y[i]-1]+=1
        red[y[i]-1]=res[y[i]-1]
    elif red[x[i]-1]==0 and red[y[i]-1]>0:
        res[x[i]-1]-=1
        res[y[i]-1]+=1
        red[y[i]-1]=res[y[i]-1]
    elif red[x[i]-1]>0 and red[y[i]-1]>0:
        res[x[i]-1]-=1
        red[x[i]-1]-=1
        res[y[i]-1]+=1
        red[y[i]-1]=res[y[i]-1]
cnt=0
for p in red:
    if p>0:
        cnt+=1
print(cnt)
