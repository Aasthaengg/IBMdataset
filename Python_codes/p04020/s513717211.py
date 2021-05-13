
n=int(input())
A=[int(input()) for _ in range(n)]
cnt=0
for i in range(n):
    cnt+=A[i]//2
    if A[i]%2==1 and i!=n-1:
        if A[i+1]>0:
            cnt+=1
            A[i+1]-=1

print(cnt)