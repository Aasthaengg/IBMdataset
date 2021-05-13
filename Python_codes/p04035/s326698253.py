n,l = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]

index = 0
for i in range(n-1):
    if a[i]+a[i+1] >= l:
        index = i+1

if index==0:
    print("Impossible")
else:
    print("Possible")
    for i in range(1,index):
        print(i)
    for i in range(n-1,index,-1):
        print(i)
    print(index)