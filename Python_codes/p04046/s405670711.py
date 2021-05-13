h,w,a,b=map(int,input().split())

U = 2*10**5
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
  x = fact[n]
  x *= fact_inv[k]
  x %= MOD
  x *= fact_inv[n-k]
  x %= MOD
  return x
ans=0
mod=10**9+7
for i in range(1,h-a+1):
    ans+=(comb(i+b-2,min(i-1,b-1))*comb(h-i+w-b-1,min(h-i,w-b-1)))%mod
    ans=ans%mod
print(ans)


