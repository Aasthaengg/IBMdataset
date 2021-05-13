N,M=map(int,input().split())
Red=[False]*N
Cnt=[1]*N
Red[0]=True
for i in range(M):
    x,y=map(lambda x:int(x)-1,input().split())
    Red[y]|=Red[x]
    Cnt[y]+=1
    Cnt[x]-=1
    if Cnt[x]==0:
        Red[x]=False
ans=0
for i in range(N):
    if Red[i] and Cnt[i]>0:
        ans+=1
print(ans)