class Combination():
    def __init__(self,n,mod):
        self.mod = mod
        self.factorial = [0 for _ in range(n+1)]
        self.inv = [0 for _ in range(n+1)]
        self.factorial[0] = 1
        self.inv[0] = 1
        for i in range(n):
            self.factorial[i+1] = self.factorial[i]*(i+1)%mod
            self.inv[i+1] = self.inv[i]*pow(i+1,mod-2,mod)%mod
    def comb(self,m,k):
        return self.factorial[m]*self.inv[k]*self.inv[m-k]%self.mod
        
MOD = 10**9+7
H,W,A,B = map(int,input().split())

cb = Combination(H+W,MOD)

ans = 0

for i in range(H-A):
    ans += cb.comb(B-1+i,i)*cb.comb(W-B-1+H-i-1,H-i-1)
    ans %= MOD
    
print(ans)