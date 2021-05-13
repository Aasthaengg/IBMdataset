N,L=map(int,input().split())
a=list(map(int,input().split()))
suma=sum(a)
flag=0
for i in range(1,N):
    if a[i]+a[i-1]>=L:
        flag=1
        idx=i
        break
if flag:
    print("Possible")
    for i in range(1,N):
        if idx==i:
            break
        else:
            print(i)
    for i in range(N-1,0,-1):
        if idx==i:
            break
        else:
            print(i)
    print(idx)
else:
    print("Impossible")
