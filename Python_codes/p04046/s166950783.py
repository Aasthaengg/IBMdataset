from operator import mul
from functools import reduce
from functools import lru_cache


H,W,A,B = map(int,input().split())
ans = 0
mod = 10**9+7

lru_cache(maxsize=None)
def cmb(c, r):
    return fc[c + r] * ic[c] * ic[r] % mod
 
fc = [1] * (H + W)
for i in range(2, H+W):
    fc[i] = fc[i - 1] * i % mod
ic = [pow(x, mod-2, mod) for x in fc]
 
if H-A <= W-B:
    for i in range(0,H-A):
        ans += cmb(i, B-1) * cmb(H - 1 - i,W - 1 -B ) % mod
else:
    for i in range(B, W):
        ans += cmb(i, H - 1 - A) * cmb(W - 1 - i, A - 1) % mod
  
print(ans%(mod))