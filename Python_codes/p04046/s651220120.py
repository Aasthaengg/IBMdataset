def cmb(a, b, fact, mod):
    return fact[a] * pow(fact[b], mod - 2, mod) * pow(fact[a - b], mod - 2, mod) % mod


def main():
    h, w, a, b = map(int, input().split())
    mod = 10 ** 9 + 7

    fact = [1] * (h + w + 1)
    for i in range(1, h + w + 1):
        fact[i] = (fact[i - 1] * i) % mod

    ans = 0
    for i in range(b, w):
        ans += cmb(h - a + i - 1, i, fact, mod) * cmb(w - 1 - i + a - 1, w - i - 1, fact, mod) % mod
    print(ans % mod)

if __name__ == '__main__':
    main()

