fact = [1]
invfact = [1]
mod = 10 ** 9 + 7
h, w, a, b = map(int, input().split())
for i in range(1, h+w+1):
    fact.append((fact[-1] * i) % mod)
    invfact.append(pow(fact[i], mod - 2, mod))

ans = 0
for i in range(b, w):
    ans += (fact[h - a - 1 + i] * invfact[h - a - 1] * invfact[i]) * \
        (fact[a - 2 + w - i] * invfact[a - 1] * invfact[w - i-1])
    ans %= mod
print(ans)
