N, L = map(int, input().split())
a = [int(i) for i in input().split()]

max_k = 0
max_p = 0

for i in range(N-1):
    if a[i]+a[i+1] > max_k:
        max_k = a[i]+a[i+1]
        max_p = i+1

if max_k < L:
    print('Impossible')
    exit()
else:
    print('Possible')

for i in range(1, N):
    if i == max_p:
        break
    else:
        print(i)

for i in range(N-1, 0, -1):
    if i == max_p:
        print(i)
        exit()
    else:
        print(i)
