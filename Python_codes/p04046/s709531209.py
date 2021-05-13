MOD = 10**9 + 7
factorials = [1]
for i in range(1, 200000):
    factorials.append((factorials[-1] * i) % MOD)
invs = [pow(x, MOD - 2, MOD) for x in factorials]


def combinations(n, k):
    return (factorials[n] * invs[k] * invs[n - k]) % MOD


def f(x, y):
    return combinations(x + y - 2, x - 1)


h, w, a, b = map(int, input().split())
res = 0
for y in range(1, h - a + 1):
    res += (f(b, y) * f(w - b, h - y + 1)) % MOD
print(res % MOD)