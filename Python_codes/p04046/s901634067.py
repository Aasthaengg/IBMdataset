H, W, A, B = map(int, input().split())
MAX = 200000
MOD = 1000000007
fac = [0]*MAX
finv = [0]*MAX
inv = [0]*MAX
fac[0] = 1
fac[1] = 1
finv[0] = 1
finv[1] = 1
inv[1] = 1
for i in range(2, MAX):
  fac[i] = fac[i-1]*i%MOD
  inv[i] = MOD - inv[MOD%i]*(MOD//i)%MOD
  finv[i] = finv[i-1]*inv[i]%MOD  
# sum_{i=B}^{W-1} C_{H-A-1+i}_{i}C_{A+W-i-2}_{A-1}
r = 0
for i in range(B, W):
  r += fac[H-A-1+i]*(finv[H-A-1]*finv[i]%MOD)%MOD * fac[A+W-i-2]*(finv[A-1]*finv[W-1-i]%MOD)%MOD
  r = r%MOD
print(r)
