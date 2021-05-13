N,L = map(int,input().split())
A = list(map(int,input().split()))
A.insert(0,0)
cmax = 0
ind = -1
for i in range(1,N):
    if A[i]+A[i+1]>cmax:
        cmax = A[i]+A[i+1]
        ind = i
if cmax>=L:
    print("Possible")
    for i in range(1,ind):
        print(i)
    for i in range(N-1,ind-1,-1):
        print(i)
else:
    print("Impossible")