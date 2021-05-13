h, w, a, b = map(int, input().split())

N = h + w

def power(x, y):
    if   y == 0     : return 1
    elif y == 1     : return x % mod
    elif y % 2 == 0 : return power(x, y // 2) ** 2 % mod
    else            : return power(x, y // 2) ** 2 * x % mod

mod = 10 ** 9 + 7

factorial = [1]
for i in range(1, N):
    factorial.append(factorial[i - 1] * i % mod)

inverseFactorial = [0] * N
inverseFactorial[N - 1] = power(factorial[N - 1], mod - 2)
for i in range(N - 2, -1, -1):
    inverseFactorial[i] = inverseFactorial[i + 1] * (i + 1) % mod

def comb(x, y):
    return factorial[x] * inverseFactorial[y] * inverseFactorial[x - y] % mod



ans = 0
for i in range(1, h - a + 1):
    ans += comb(b + i - 2, b - 1) * comb(h - i + w - b - 1, w - b - 1)
    # print(i, ans)
    ans %= mod
print(ans)
