def nCr(n, r):
	global fact, inv, MOD
	return (fact[n] * inv[n-r] * inv[r]) % MOD

MOD = 1000000007
MAX = 200001

h, w, a, b = map(int, input().split())

fact = [1 for i in range(MAX)]
inv = [1 for i in range(MAX)]

for i in range(1, MAX):
	fact[i] = (fact[i-1] * i) % MOD
	inv[i] = pow(fact[i], MOD-2, MOD)

ans = 0
for i in range(h - a):
	t = nCr(b-1+i, b-1) * nCr(w-1-b + h-1-i, w-1-b)
	ans = (ans + t) % MOD

print(ans)