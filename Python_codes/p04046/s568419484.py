h, w, a, b = map( int, input().split() )

SIZE = h+w+2
MOD = 10**9 + 7
MOD_Farmer = 10**9+5

fact = [0] * SIZE
inv = [0] * SIZE
fact_inv = [0] * SIZE

# prepare --------------------------------
inv[0] = 0
inv[1] = 1
fact[0] = fact[1] = 1
fact_inv[0] = fact_inv[1] = 1
for i in range( 2, SIZE ):
  inv[i] = MOD - (MOD//i)*inv[MOD%i]%MOD
  fact[i] = fact[i-1] * i % MOD
  fact_inv[i] = fact_inv[i-1] * inv[i] % MOD
#  fact_inv[i] = fact[i] **( 10**4 ) \
#              * fact[i] **( 10**5 ) \
#              * fact[i] ** 5 % MOD % MOD
# ----------------------------------------
def comb( n, r ):
  if r >= 0 and n >= 0:
    return fact[n] * fact_inv[n-r]%MOD * fact_inv[r]%MOD
  else :
    return 0.0
# ----------------------------------------

#print( fact_inv )

ans = 0
for i in range( h-a ):
    ans += comb(i+b-1, b-1) * comb(h-i-1+w-b-1,w-b-1)
    ans %= MOD
print( ans )