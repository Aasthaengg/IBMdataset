n,l = map(int,input().split())
al = list(map(int,input().split()))

target = -1
for i in range(n-1):
    if al[i] + al[i+1] >= l:
        target = i

if target == -1:
    print("Impossible")
    exit()
else:
    print("Possible")
    for i in range(target):
        print(i+1)
    for i in range(n-1, target+1, -1):
        print(i)
    print(target+1)

