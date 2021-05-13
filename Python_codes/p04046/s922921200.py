mod = 10**9+7
h, w, a, b = map(int, input().split())

n = h+w-2

ans = 0
fac = [1]*(n+1)
inv = [1]*(n+1)

for i in range(1, n+1):
    fac[i] = i*fac[i-1] % mod

for i in range(1, n+1):
    inv[i] = pow(fac[i], mod-2, mod)

def func(x, y):
    m = fac[x+y]*inv[x]*inv[y]%mod
    return m

for x in range(b, w):
    ans += func(x, h-a-1)*func(w-1-x, a-1)
    ans %= mod

print(ans)
