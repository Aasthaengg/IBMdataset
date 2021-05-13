N,L=map(int,input().split())
A=list(map(int,input().split()))
flag=False
for i in range(N-1):
    if A[i]+A[i+1]>=L:
        flag=True
        idx=i+1
        break
if not flag:
    print('Impossible')
else:
    print('Possible')
    for i in range(1,idx):
        print(i)
    for i in range(N-1,idx,-1):
        print(i)
    print(idx)