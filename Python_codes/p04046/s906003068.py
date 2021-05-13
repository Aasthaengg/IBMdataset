class Factorials:
    # nに十分大きい数を入力
    def __init__(self, n, mod):
        self.mod = mod

        # self.fac[i] ≡ i! (factorial:階乗)
        self.fac = [1]
        num = 1
        for i in range(1, n+1):
            num *= i
            num %= mod
            self.fac.append(num)

        # self.rec[i] ≡ 1 / i! (reciprocal:逆数)
        num = pow(num, mod-2, mod)
        self.rec = [1 for i in range(n+1)]
        self.rec[n] = num
        for i in range(n-1, 0, -1):
            num *= i + 1
            num %= mod
            self.rec[i] = num

    # comb(n, r) ≡ nCr
    def comb(self, n, r):
        return self.fac[n] * self.rec[r] * self.rec[n - r] % self.mod
    
    # perm(n, r) ≡ nPr
    def perm(self, n, r):
        return self.fac[n] * self.rec[n-r] % self.mod

    # fact(n) ≡ n!
    def fact(self, n):
        return self.fac[n]

h, w, a, b = map(int, input().split())
mod = 10**9 + 7

f = Factorials(2 * (10 ** 5), mod)
if h - a < w - b:
    num = h - a
else:
    num = w - b

ans = 0
for i in range(num):
    x = h - a - i
    y = b + i + 1

    ans += f.comb(x + y - 2, x - 1) * f.comb(h + w - x - y, h - x)
    ans %= mod

print(ans)