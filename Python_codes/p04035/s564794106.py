n,l = map(int,input().split())
a = list(map(int,input().split()))

memo = -1
for i in range(n-1):
    if a[i]+a[i+1] >= l:
        memo = i

if memo == -1:
    print("Impossible")
else:
    print("Possible")
    for i in range(memo):
        print(i+1)
    for i in range(n-2,memo-1,-1):
        print(i+1)


