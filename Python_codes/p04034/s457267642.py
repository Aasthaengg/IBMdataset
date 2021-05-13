N,M=map(int, input().split())

prob=[0]*N
prob[0]=1
num=[1]*N
num[0]=1

for i in range(M):
    x,y=map(int, input().split())
    if prob[x-1]==1:
        prob[y-1]=1
    num[x-1]-=1
    num[y-1]+=1
    if num[x-1]==0:
        prob[x-1]=0
print(sum(prob))