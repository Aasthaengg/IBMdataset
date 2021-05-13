n,l = map(int,input().split())
a = list(map(int,input().split()))
for N in range(n - 1):
    a[N] = a[N] + a[N + 1]
if max(a) >= l:
    print('Possible')
    ind = a.index(max(a)) + 1
    for  i in range(ind - 1):
        print(i + 1)
    for i in range(n - ind):
        print(n - i - 1)
else:
    print('Impossible')