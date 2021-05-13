
a,b,c,d = list(map(int, input().split()))

def cmb(n, r, p):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n-r] % p

p = 10**9+7
N = 10 ** 6 + 2
fact = [1, 1]  # fact[n] = (n! mod p)
factinv = [1, 1]  # factinv[n] = ((n!)^(-1) mod p)
inv = [0, 1]  # factinv 計算用

for i in range(2, N + 1):
    fact.append((fact[-1] * i) % p)
    inv.append((-inv[p % i] * (p // i)) % p)
    factinv.append((factinv[-1] * inv[-1]) % p)
    
def wh(w,h):
    return cmb(w+h,w,10**9+7)

ans = wh(b-1,a-1)
#print(ans)

for i in range(d):
    tmp = wh(i,a-c-1) * wh(c-1,b-i-1) % p
    ans += p
    ans -= tmp
    ans %= p
    #print(ans)
    
print(ans)


