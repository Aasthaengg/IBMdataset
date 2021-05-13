N,M=map(int,input().split())
R=[True]+[False]*(N-1)
B=[1]*N
for i in range(M):
    x,y=map(int,input().split())
    if R[x-1]:
        R[y-1]=True
    B[x-1]-=1
    B[y-1]+=1
    if B[x-1]==0:
        R[x-1]=False
print(R.count(True))