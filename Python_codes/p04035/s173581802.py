N,L=map(int,input().split())
a=[int(i) for i in input().split()]
j=-1
for i in range(N-1):
    if a[i]+a[i+1]>=L:
        j=i
        break
if j==-1:
    print("Impossible")
else:
    print("Possible")
    for i in range(j):
        print(i+1)
    for i in range(j+1,N-1)[::-1]:
        print(i+1)
    print(j+1)
