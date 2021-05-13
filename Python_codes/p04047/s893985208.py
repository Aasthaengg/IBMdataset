"#!/usr/bin/env python3"

N = int(input())
L = list(map(int,input().split()))

L = sorted(L)

ans = 0
for i in range(0, 2*N, 2) :
    ans += L[i]

print(ans)
