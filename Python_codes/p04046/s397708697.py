h,w,a,b = map(int,input().split())

MOD = 1000000007
fac = [1]
inv = [1]
for i in range(1,200010):
	fac.append(fac[i-1]*i%MOD)
	inv.append(pow(fac[i],MOD-2,MOD))

ans = 0

for i in range(b+1,w+1):
	ans += fac[h-a+i-2]*inv[h-a-1]*inv[i-1]*fac[a+w-i-1]*inv[a-1]*inv[w-i]%MOD
	ans %= MOD

print(ans)