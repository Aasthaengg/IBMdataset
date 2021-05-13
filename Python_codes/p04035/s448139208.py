n, l = map(int, input().split())
a = list(map(int, input().split()))
ind = -1
for i in range(n-1):
    if a[i]+a[i+1] >= l:
        ind = i
        break

if ind == -1:
    print("Impossible")
else:
    print("Possible")
    for i in range(ind):
        print(i+1)
    for i in range(n-1, ind, -1):
        print(i)
