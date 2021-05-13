N=int(input())
A=[int(input()) for _ in range(N)]
cnt=0
buf=0
#print(A)
if N==1:
    print(A[0]//2)
else:
    for i in range(N-1):
        su=A[i]+A[i+1]
        cnt=cnt+su//2
        buf=(su//2)*2
        if buf>A[i]:
            A[i+1]=A[i+1]-(buf-A[i])
            A[i]=0
        else:
            A[i]=A[i]-buf
    #print(A,cnt)
    print(cnt)