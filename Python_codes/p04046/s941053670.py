# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 17:33:45 2019
ABC042D
@author: maezawa
"""

MAX = 5*10**5+1
MOD = 10**9+7

fac = [0] * MAX
finv = [0]*MAX
inv = [0]*MAX

# テーブルを作る前処理
fac[0] = 1
fac[1] = 1
finv[0] = 1
finv[1] = 1
inv[1] = 1
for i in range(2,MAX):
    fac[i] = fac[i - 1] * i % MOD
    inv[i] = MOD - inv[MOD%i] * (MOD // i) % MOD
    finv[i] = finv[i - 1] * inv[i] % MOD

# 二項係数計算
def COM(n, k):
    if (n < k):
        return 0
    if (n < 0 or k < 0):
        return 0
    return fac[n] * (finv[k] * finv[n - k] % MOD) % MOD

def HCOM(n,k):
    return COM(n+k-1,k)


#n, r = list(map(int, input().split()))
#ans = COM(n, r)
#print(ans)

h, w, a, b = list(map(int, input().split()))
cnt = 0
for i in range(h-a):
    p0 = HCOM(b, i) * HCOM(w-b,h-i-1)
    cnt = (cnt+p0)%MOD
print(cnt)