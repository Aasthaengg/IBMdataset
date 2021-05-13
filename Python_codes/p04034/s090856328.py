N,M=map(int,input().split())
num=[1]*N
ex=[0]*N
ex[0]=1
P=[]
ans=1
for i in range(M):
    x,y=map(int,input().split())
    num[x-1]-=1
    num[y-1]+=1
    if ex[x-1]==1 and ex[y-1]==0:
        ex[y-1]=1
    if num[x-1]==0:
        ex[x-1]=0
print(sum(ex))