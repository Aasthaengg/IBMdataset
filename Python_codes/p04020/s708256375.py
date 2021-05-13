N=int(input())
A=[int(input()) for i in range(N)]
count=0
count+=A[0]//2
A[0]%=2
for i in range(1,N):
    count+=(A[i-1]+A[i])//2
    if A[i]:
        A[i]=(A[i-1]+A[i])%2
    else:
        A[i]=0
print(count)
