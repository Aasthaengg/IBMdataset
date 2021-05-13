N, L = map(int, input().split())
a = [int(x) for x in input().split()]

ans = False
for i in range(N-1):
    if a[i] + a[i+1] >= L:
        ans = True
        break
if ans:
    print('Possible')
    for j in range(i):
        print(j+1)
    for j in range(N-2, i-1, -1):
        print(j+1)
else:
    print('Impossible')