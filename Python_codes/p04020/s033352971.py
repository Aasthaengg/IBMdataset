N=int(input())
A=[int(input()) for i in range(N)]
ans=0
for i in range(N):
    ans+=A[i]//2
    A[i]-=(A[i]//2*2)
    if i>0:
        d=min(A[i],A[i-1])
        ans+=d
        A[i]-=d
        A[i-1]-=d
    if i<N-1:
        d=min(A[i],A[i+1])
        ans+=d
        A[i]-=d
        A[i+1]-=d
print(ans)