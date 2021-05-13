import sys
N, L = map(int, input().split())
a = list(map(int, input().split()))

last = -1
for i in range(N-1):
    if a[i] + a[i+1] >= L:
        last = i
        break
if last == -1:
    print('Impossible')
    sys.exit()

print('Possible')
for i in range(last): print(i+1)
for i in range(N-1, last, -1): print(i)