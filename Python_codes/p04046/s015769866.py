high, width, y, x = map(int, input().split())

def nCr(n, r):
    return ((((fact[n]*finv[n-r])%mod)*finv[r])%mod)

mod = 10**9 + 7
inv = mod - 2
maxn = high + width - 2
fact = [0] * (maxn+1)
finv = [0] * (maxn+1)
fact[0] = fact[1] = 1
finv[0] = finv[1] = 1

# 階乗を求める
for i in range(2, maxn+1):
    fact[i] = (fact[i-1] * i) % mod

# 階乗の逆元を求める
for i in range(2, maxn+1):
    finv[i] = pow(fact[i], inv, mod)

route = 0
for i in range(1, high-y+1):
        route += (nCr(x+i-2, i-1) * nCr(width+high-x-1-i, high-i)) % mod
        route = route % mod
print(int(route))