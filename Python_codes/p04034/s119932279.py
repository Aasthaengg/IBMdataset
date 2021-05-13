n,m=map(int,input().split())
cnt=[1]*n
yn=[0]*n
yn[0]=1
for i in range(m):
    x,y=map(int,input().split())
    cnt[x-1]-=1
    cnt[y-1]+=1
    if x==1:
        if cnt[0]==0:
            yn[0]=0
        yn[y-1]=1
        for j in range(i+1,m):
            x,y=map(int,input().split())
            if yn[x-1]==1:
                yn[y-1]=1
            if cnt[x-1]==1:
                yn[x-1]=0
            cnt[x-1]-=1
            cnt[y-1]+=1
        break
print(yn.count(1))
