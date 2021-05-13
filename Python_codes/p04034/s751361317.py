n,m=map(int,input().split())
x=[]
y=[]
for i in range(m):
    xy=list(map(int,input().split()))
    x.append(xy[0]-1)
    y.append(xy[1]-1)

red=[0]*n
red[0]=1
cnt=[1]*n

for i in range(m):
    cnt[x[i]]-=1
    cnt[y[i]]+=1

    if red[x[i]]==1:
        red[y[i]]=1
    
    if cnt[x[i]]==0:
        red[x[i]]=0

ans=0
for i in range(n):
    if red[i]==1 and cnt[i]>0:
        ans+=1

print(ans)