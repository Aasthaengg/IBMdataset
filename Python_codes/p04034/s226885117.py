N,M=map(int,input().split())
box=[1 for _ in range(N)]
ans=[0 for _ in range(N)]
ans[0]=1
for i in range(M):
    x,y=map(int,input().split())
    box[x-1]-=1
    box[y-1]+=1
    if ans[x-1]==1:
        ans[y-1]=1
    if box[x-1]==0:
        ans[x-1]=0
print(sum(ans))