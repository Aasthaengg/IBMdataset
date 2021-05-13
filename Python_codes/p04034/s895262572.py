n,m=map(int, input().split())
aka = [0]*(n+1)
siroaka = [1]*(n+1)
aka[1] = 1
for i in range(m):
    x,y=map(int, input().split())
    siroaka[x]-=1
    siroaka[y]+=1
    if(aka[x]):
        aka[y]=1
    if(siroaka[x]==0):
        aka[x]=0

print(sum(aka))
