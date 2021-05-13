#Combinationクラス
class Combination:

    def __init__(self, n, MOD):
        self.fact = [1]
        for i in range(1, n + 1):
            self.fact.append(self.fact[-1] * i % MOD)
        self.inv_fact = [pow(self.fact[i] ,MOD - 2 ,MOD) for i in range(n + 1)]
        self.MOD = MOD

    def factorial(self, k):
        '''k!を求める'''
        return self.fact[k]

    def inverse_factorial(self, k):
        '''k!の逆元を求める'''
        return self.inv_fact[k]

    def combination(self, k, r):
        '''kCrを求める'''
        return (self.fact[k] * self.inv_fact[k - r] * self.inv_fact[r]) % self.MOD


h, w, a, b = map(int,input().split())
MOD = 10**9 + 7
comb = Combination(h+w, MOD)
ans = 0
for i in range(0, h-a):
    ans += comb.combination((b-1)+i,i) * comb.combination((w-b-1)+(h-i-1), w-b-1)
    ans = ans % MOD
print(ans)