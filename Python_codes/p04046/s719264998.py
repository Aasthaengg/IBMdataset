def solve():
	h,w,a,b = map(int, input().split())
	mx = max(h,w)
	mod = 10**9+7
	fac = [1]*(h+w+1)
	for i in range(1,h+w+1):
		fac[i]=fac[i-1]*i%mod
	inv = [1]*(mx+1)
	inv[-1] = pow(fac[mx], mod-2, mod)
	for i in range(mx-1, -1, -1):
		inv[i] = inv[i+1]*(i+1)%mod
	const = inv[h-a-1]*inv[a-1]%mod
	ans = sum(fac[h-a+i-1]*inv[i]*fac[a+w-2-i]*inv[w-i-1]%mod for i in range(b,w))
	print(ans*const%mod)

if __name__=="__main__":solve()