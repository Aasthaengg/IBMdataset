N, L = map(int, input().split())
A = list(map(int, input().split()))
k = -1
for i in range(N-1):
    if A[i]+A[i+1]>=L:
        k=i+1
if k==-1:
    print("Impossible")
else:
    print("Possible")
    res = []
    for i in reversed(range(1,k+1)):
        res.append(i)
    for i in range(k+1,N):
        res.append(i)
    for i in reversed(res):
        print(i)