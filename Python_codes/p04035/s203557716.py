N,L = map(int,input().split())
A = list(map(int,input().split()))
A.insert(0,0)
flag = 0
for i in range(1,N):
    if A[i]+A[i+1]>=L:
        flag = i
        break
if flag == 0:
    print("Impossible")
else:
    print("Possible")
    if flag==1:
        for i in range(N-1,0,-1):
            print(i)
    else:
        for i in range(1,flag):
            print(i)
        for i in range(N-1,flag-1,-1):
            print(i)