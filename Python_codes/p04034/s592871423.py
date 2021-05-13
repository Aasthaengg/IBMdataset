n,m=map(int,input().split())
quant=[1]*(n+1)
prob=[0]*(n+1)
prob[1]=1
for i in range(m):
    x,y=map(int,input().split())
    quant[x]-=1
    quant[y]+=1
    if prob[x]>0:
        prob[y]+=1
    if quant[x]==0:
        prob[x]=0

cnt=0
for i in range(n+1):
    if prob[i]>0:
        cnt+=1
print(cnt)
        
