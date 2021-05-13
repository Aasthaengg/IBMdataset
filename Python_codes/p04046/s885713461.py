H, W, A, B = map(int, input().split())

m = 10**9 + 7

import functools
@functools.lru_cache(maxsize=None)
def cr(c, r):
    return fc[c + r] * ic[c] * ic[r] % m

fc = [1] * (H + W)
for i in range(2, H+W):
    fc[i] = fc[i - 1] * i % m
ic = [pow(x, m-2, m) for x in fc]

ans = 0
for c in range(B, W):
    ans += cr(c, H - 1 - A) * cr(W - 1 - c, A - 1) % m
print(ans % m)