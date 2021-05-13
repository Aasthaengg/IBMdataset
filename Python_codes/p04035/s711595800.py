n,l = map(int, input().split())
a = list(map(int, input().split()))

x = -1

for i in range(n-1):
    if a[i]+a[i+1] >= l:
        x = i+1
        break

if x == -1:
    print('Impossible')
else:
    print('Possible')
    for i in range(1,x):
        print(i)
    for i in range(n-x):
        print(n-i-1)