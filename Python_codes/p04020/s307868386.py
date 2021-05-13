N=int(input())
A=[]
for i in range(N):
    A.append(int(input()))

ans=0
for i in range(N-1):
    x=A[i]
    ans+=x//2
    if x%2==1 and A[i+1]>=1:
        ans+=1
        A[i+1]-=1

ans+=A[N-1]//2
print(ans)
