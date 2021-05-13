N=int(input())
A=[]
B=[]
for i in range(N):
    a=int(input())
    A.append(a)
    B.append(a)

ans=0
if N==1:
    print(A[0]//2)
    exit()

for i in range(N):
    if i==(N-1):
        ans+=A[i]//2
        break
    if i==0:
        ans+=A[i]//2
        ans+=min(A[i]%2,A[i+1])
        A[i+1]=max(0,A[i+1]-A[i]%2)
        continue
    ans+=A[i]//2
    ans+=min(A[i]%2,A[i+1])
    A[i+1]=max(0,A[i+1]-A[i]%2)
print(ans)