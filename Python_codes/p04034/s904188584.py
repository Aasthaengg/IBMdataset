N,M=map(int,input().split())
li=[1]*N
ri=[0]*N
ri[0]=1

for i in range(M):
    x,y=map(int,input().split())
    if ri[x-1]==1:
        ri[y-1]=1
    li[x-1]-=1
    li[y-1]+=1
    if li[x-1]==0:
        ri[x-1]=0
print(sum(ri))