N,M=map(int,input().split())
xy=[list(map(int,input().split()))for _ in range(M)]

countR=[0]+[1]+[0]*(N-1)
countBall=[0]+[1]*N

for x,y in xy:
    countBall[x]-=1
    countBall[y]+=1
    if countR[x]>0:
        countR[y]+=1
    if countBall[x]<1:
        countR[x]=0

print(sum(r*b>0 for r,b in zip(countR,countBall)))