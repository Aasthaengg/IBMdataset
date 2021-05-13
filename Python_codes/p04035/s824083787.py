N, L = map(int, input().split())
a = list(map(int, input().split()))

ok = 0
for i in range(1, N):
    if a[i-1] + a[i] >= L:
        ok = 1
        break

if ok:
    print('Possible')
    for j in range(1, i):
        print(j)
    for j in range(N-1, i, -1):
        print(j)
    print(i)
else:
    print('Impossible')
