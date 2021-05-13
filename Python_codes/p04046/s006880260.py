h, w, a, b = [int(item) for item in input().split()]

MOD = 10**9 + 7
n = h + w 
def mod_pow(x, n):
    ans = 1
    while(n != 0):
        if n & 1:
            ans = ans * x % MOD
        x = x * x % MOD
        n = n >> 1
    return ans

fac = [1] + [0] * n
fac_inv = [1] + [0] * n
for i in range(1, n+1):
    fac[i] = fac[i-1] * (i) % MOD
    # Fermat's little theorem says
    # a**(p-1) mod p == 1
    # then, a * a**(p-2) mod p == 1
    # it means a**(p-2) is inverse element
    fac_inv[i] = fac_inv[i-1] * mod_pow(i, MOD-2) % MOD

def mod_nCr(n, r):
    if n == 0 and r == 0:
        return 1
    if n < r or n < 0:
        return 0
    tmp = fac_inv[n-r] * fac_inv[r] % MOD
    return tmp * fac[n] % MOD

if a+b > (h+w)//2:
    ans = 0
    for i in range(h-a):
        ans += mod_nCr(b-1+i, i) * mod_nCr(w-b-1 + h-1-i, h-1-i)
        ans %= MOD
else:
    ans = mod_nCr(h-1+w-1, h-1)
    for i in range(b):
        ans -= mod_nCr(h-a-1+i, i) * mod_nCr(a-1 + w-1-i, a-1)
        ans %= MOD
print(ans)