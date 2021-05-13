# coding: UTF-8
import numpy as np

MOD = int(1e+9+7)
H, W, A, B = map(int, input().split())

fact = [1]
for i in range(1, W+H-1):
    fact.append((fact[-1]*i) % MOD)

ifact = [pow(fact[-1], MOD-2, MOD)]
for i in reversed(range(1, W+H-1)):
    ifact.append((ifact[-1]*i) % MOD)
ifact.reverse()


def comb(n, r):
    return fact[n]*ifact[n-r]*ifact[r]


r = H-A-1
s = 0
for c in range(B, W):
    s += comb(c+r, r) * comb(W-c+A-2, A-1)
    s %= MOD

print(int(s))
