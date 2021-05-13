n = int(input())
A = [int(input()) for _ in range(n)]

ans = 0
for i in range(n):
    if A[i]%2==0:
        ans+=A[i]//2
    else:
        ans+=A[i]//2
        if i+1<n and A[i+1]!=0:
            A[i+1]-=1
            ans+=1
print(ans)