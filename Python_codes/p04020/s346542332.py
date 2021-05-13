n=int(input())
A=[]
for i in range(n):
    A.append(int(input()))

ans=0
for i in range(n-1):
    ans+=A[i]//2
    A[i]%=2
    if A[i]==1 and A[i+1]>0:
        ans+=1
        A[i+1]-=1

ans+=A[-1]//2
print(ans)