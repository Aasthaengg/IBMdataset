h,w,a,b = map(int,input().split())
mod = 10**9+7

MAX = 2*10**5
fact = [1]*(MAX+1)
for i in range(1, MAX+1):
    fact[i] = (fact[i-1]*i) % mod

inv = [1]*(MAX+1)
for i in range(2, MAX+1):
    inv[i] = inv[mod % i]*(mod-mod//i) % mod

fact_inv = [1]*(MAX+1)
for i in range(1, MAX+1):
    fact_inv[i] = fact_inv[i-1] * inv[i] % mod

def comb(n, k):
    if n < k:
        return 0
    return fact[n] * fact_inv[n-k] * fact_inv[k] % mod
  
ans = 0
for k in range(b+1,w+1):
  ans += comb(k+h-a-2,h-a-1)*comb(w-k+a-1,a-1)%mod
  ans %= mod
print(ans)