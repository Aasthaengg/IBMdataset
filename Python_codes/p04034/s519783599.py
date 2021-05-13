N,M=map(int,input().split())
Z=[1]*(N+1)
Z[0]=0

H=[False]*(N+1)
H[1]=True

for _ in range(M):
    X,Y=map(int,input().split())

    H[Y]|=H[X]

    Z[X]-=1
    Z[Y]+=1

    H[X]&=(Z[X]!=0)
print(sum(H))
