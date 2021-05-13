N = int(input())
A = [int(input()) for _ in range(N)]
cnt = 0
for i in range(N):
    if A[i]%2==1:
        cnt += A[i]//2
        A[i] = 1
    else:
        a = A[i]//2
        if a>0:
            cnt += a-1
            A[i] = 2
for i in range(1,N):
    if A[i-1]!=1:
        cnt += A[i-1]//2+A[i]//2
        A[i-1]=0
        A[i]=A[i]%2
    elif A[i-1]==1 and A[i]>=1:
        cnt += 1
        A[i-1]=0
        A[i] -= 1
if N==1:
    cnt = A[0]//2
print(cnt)