n, k = map(int,input().split())
a = list(map(int,input().split()))
idx = -1
for i in range(n-1):
    if a[i]+a[i+1]>=k:
        idx = i
        break
if idx == -1:
    print('Impossible')
    exit()
else:
    print('Possible')
    for i in range(1, idx+1):
        print(i)
    for i in range(n-1, idx, -1):
        print(i)