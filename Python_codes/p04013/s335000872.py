class Combination:
    def __init__(self, n, mod):
        self.n = n
        self.mod = mod
        self.fac = [1 for i in range(self.n + 1)]
        self.finv = [1 for i in range(self.n + 1)]
        for i in range(2, self.n+1):
            self.fac[i] = (self.fac[i - 1] * i) % self.mod
            self.finv[i] = (self.finv[i-1] * pow(i, -1, self.mod)) % self.mod

    def comb(self, n, m):
        return self.fac[n] * (self.finv[n-m] * self.finv[m] % self.mod) % self.mod
def iparse():
    return list(map(int, input().split()))

if __name__ == "__main__":
    n, a = iparse()
    x = iparse()

    dp = [[[0 for i in range(sum(x) + 10)] for j in range(n + 10)] \
        for k in range(n + 10)]
    dp[0][0][0] = 1
    for i in range(n):
        for j in range(n + 1):
            for k in range(sum(x) + 1):
                if j >= 1 and k - x[i] >= 0:
                    dp[i + 1][j][k] = dp[i][j][k] + dp[i][j - 1][k - x[i]]
                else:
                    dp[i+1][j][k] = dp[i][j][k]
    ans = 0
    for i in range(n):
        if (i + 1) * a >= sum(x) + 10:
            break
        ans += dp[n][i + 1][(i+1)*a]
    print(ans)
    
