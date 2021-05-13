N=int(input())
A=[0]
for i in range(1,N+1):
    A.append(int(input()))

ans=0
i=1
while i<=N:
    # print(i)
    # print(A[1:])
    if A[i]>=2:
        ans+=A[i]//2
        A[i]%=2
    # print(A[1:])
    if i<N and A[i]==1 and A[i+1]>=1:
        ans+=1
        A[i]-=1
        A[i+1]-=1
    # print(A[1:])
    # print(ans)
    i+=1

print(ans)
