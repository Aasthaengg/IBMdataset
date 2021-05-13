N,L=map(int,input().split())
A=list(map(int,input().split()))
sum_A=sum(A)

junban=[]
flg=False

for i in range(N-1):
    if A[i]+A[i+1]>=L:
        tmp=i
        flg=True


if flg:
    print("Possible")
    for i in range(N-1):
        if tmp>i:
            print(i+1)
        else:
            print(N+tmp-i-1)
else:
    print("Impossible")