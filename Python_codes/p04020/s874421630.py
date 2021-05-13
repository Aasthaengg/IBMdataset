N=int(input())
A=[int(input()) for _ in range(N)]

ans=A[0]//2
res=A[0]%2
for i in range(1,N):
    ans+=(A[i]+res)//2
    if A[i]>0:
        res=(A[i]+res)%2
    else:
        res=0
print(ans)