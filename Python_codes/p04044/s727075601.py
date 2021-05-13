# -*- coding: utf-8 -*-

N, L = map(int, input().split())
S = []
for i in range(N):
    S.append(input())

S_sorted = sorted(S)
ans = "".join(S_sorted)
print(ans)
