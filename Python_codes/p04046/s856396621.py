U = 2*10**6
MOD = 10**9+7
 
fact = [1]*(U+1)
fact_inv = [1]*(U+1)
 
for i in range(1,U+1):
  fact[i] = (fact[i-1]*i)%MOD
fact_inv[U] = pow(fact[U],MOD-2,MOD)
 
for i in range(U,0,-1):
  fact_inv[i-1] = (fact_inv[i]*i)%MOD
 
def comb(n,k):
  if k < 0 or k > n:
    return 0
  z = fact[n]
  z *= fact_inv[k]
  z %= MOD
  z *= fact_inv[n-k]
  z %= MOD
  return z

h, w, a, b = map(int, input().split())
ans = 0
for i in range(h-a):
  ans += comb(b+i-1, i) * comb(w+h-b-i-2, h-i-1)
  ans %= MOD
print(ans)