h, w, a, b = map(int, input().split())

mod = 10**9+7
fac = [1]
for n in range(1, h+w):
	fac.append(fac[n-1]*n%mod)

def modpow(a,n,mod):
	r=1
	while n>0:
		if n&1:	r = r*(a%mod)
		a *= a%mod
		n >>= 1
	return r

invfac = [0] * (h+w)
invfac[h+w-1] = modpow(fac[h+w-1], mod-2, mod)
for n in range(h+w-2, -1, -1):
	invfac[n] = invfac[n+1] * (n+1) % mod

def com(a,b):
	return fac[a] * invfac[b] * invfac[a-b] % mod

r=0
for i in range(w-b):
	r += com( h-a-1+b+i, b+i ) * com( a-1+w-b-i-1, a-1 ) % mod
	r %= mod

print(r)
