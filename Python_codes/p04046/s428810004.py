h, w, a, b = map(int, input().split())

MOD = 10 ** 9 + 7

class ModCmb:
    def __init__(self, size):
        self.inv = [1] * (size + 1)
        self.fact = [1] * (size + 1)
        temp_inv = [1] * (size + 1)
        for i in range(2, size + 1):
            temp_inv[i] = ( -(MOD // i) * temp_inv[MOD%i] ) % MOD
        for i in range(2, size + 1):
            self.fact[i] = self.fact[i-1] * i % MOD
            self.inv[i] = self.inv[i-1] * temp_inv[i] % MOD

    def cmb(self, n, r):
        #print(n, r)
        if n <= 1 or n == r:
            return 1
        elif r == 1:
            return n
        res = (self.fact[n] * self.inv[r] % MOD ) * self.inv[n-r] % MOD
        #print(res)
        return res

c = ModCmb(h+w)

ans = 0
x = h-a-1
y = w-b-1
for i in range(h-a):
    j = h+w-2-i-b
    #print(i, j)
    #print(i+b-1, b-1, j, w-b-1)
    ans += c.cmb(i+b-1, b-1) * c.cmb(j, w-b-1)
    ans %= MOD

print(ans % MOD)
