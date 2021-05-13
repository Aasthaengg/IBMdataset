h, w, a, b = [int(i) for i in input().split()]

mod = 10 ** 9 + 7
kkai = [1]
for i in range(1, 210000):
    kkai.append(kkai[-1] * i % mod)


def kai(x, p=mod):
    return kkai[x]


def comb(a, b, p=mod):
    if a < 0 or b < 0:
        return 0
    elif a < b:
        return 0
    c = 1
    c *= kai(a, p)
    c *= pow(kai(b, p), p - 2, p)
    c *= pow(kai(a - b, p), p - 2, p)
    return c % p


ans = 0
for i in range(b, w):
    ans += comb(i+(h-a)-1, i)*comb((w-i)+a-2, a-1)
    ans %= mod
print(ans)
