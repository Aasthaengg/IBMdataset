h,w,a,b = map(int, input().split())

mod = 10**9 + 7
n = 10**5 * 2 + 1

fact = [1]*(n+1)
rfact = [1]*(n+1)
r = 1
for i in range(1, n+1):
  fact[i] = r = r * i % mod
rfact[n] = r = pow(fact[n], mod-2, mod)
for i in range(n, 0, -1):
  rfact[i-1] = r = r * i % mod

# nPk (mod MOD) を求める
def perm(n, k):
  return fact[n] * rfact[n-k] % mod

# nCk (mod MOD) を求める
def comb(n, k):
  return fact[n] * rfact[k] * rfact[n-k] % mod 
ans = 0
for i in range(b,w):
  ans = (ans + comb(h-a-1+i,i) * comb(w-i+a-2,a-1)) % mod
print(ans)