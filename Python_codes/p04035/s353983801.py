#!/usr/bin/env python3

N, L = map(int, input().split())
a = list(map(int, input().split()))

sums = [a[i]+a[i+1] for i in range(N-1)]

maxind, maxval = max(enumerate(sums), key=lambda x:x[1])
if maxval >= L:
    print("Possible")
    for i in range(maxind):
        print(i+1)
    for j in reversed(range(maxind, N-1)):
        print(j+1)
else:
    print("Impossible")
