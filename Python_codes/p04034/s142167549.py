n,m=map(int,input().split())
kosuu=[0]+[1]*n
haitteru=[0]+[1]+[0]*(n-1)
for _ in range(m):
    x,y=map(int,input().split())
    if haitteru[x]==1:
        kosuu[x]-=1
        kosuu[y]+=1
        haitteru[y]=1
        if kosuu[x]==0:
            haitteru[x]=0
    else:
        kosuu[x]-=1
        kosuu[y]+=1
print(haitteru.count(1))
