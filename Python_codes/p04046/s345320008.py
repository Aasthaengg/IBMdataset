from array import *
import time
h, w, a, b = map(int, input().split(' '))
MOD = 10**9 + 7
MAX = max(h+w-a-1, a+w)


def modpow(a, b):
    res = 1
    while b:
        if (b & 1):
            res = (res * a) % MOD
        a = (a * a) % MOD
        b >>= 1
    return res


def nCr(n, r):
    if r == 0 or n == r:
        return 1
    return (((f[n] * ivf[n-r]) % MOD) * ivf[r]) % MOD


f = [1] * MAX
f = array('q', f)
ivf = [0] * MAX
ivf = array('q', ivf)
for i in range(1, MAX):
    f[i] = (f[i-1] * i) % MOD
    ivf[i] = modpow(f[i], MOD-2)
r = 0
for i in range(b, w):
    y1 = h - a - 1
    x1 = i
    y2 = a - 1
    x2 = w - i - 1
    p = (nCr(x1 + y1, x1) * nCr(x2 + y2, x2)) % MOD
    r = (r + p) % MOD
print(int(r))
