N,M=map(int,input().split(' '))
B = [1]*N
R = [1]+[0]*(N-1)
for i in range(M):
    x,y=map(lambda x:int(x)-1,input().split(' '))
    B[x]-=1
    B[y]+=1
    if R[x] and B[x]:
        R[y]=1
    elif R[x] and not B[x]:
        R[x]=0
        R[y]=1
print(sum(R))