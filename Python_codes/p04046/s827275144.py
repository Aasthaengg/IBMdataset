import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def comb_mod(n, r):
    res = 1
    r = min(n - r, r)

    for i in range(r):
        res *= (n - i)
        res %= MOD
        res *= pow((r - i), MOD - 2, MOD)

    return res


def main():
    h, w, a, b = map(int, readline().split())

    ans = 0
    comb1 = 1
    comb2 = comb_mod(w - b - 1 + h - 1, w - b - 1)

    for i in range(h - a):
        ans += comb1 * comb2
        ans %= MOD
        comb1 *= (b - 1 + i + 1)
        comb1 %= MOD
        comb1 *= pow(i + 1, MOD - 2, MOD)
        comb1 %= MOD
        comb2 *= pow(w - 1 - b + h - 1 - i, MOD - 2, MOD)
        comb2 %= MOD
        comb2 *= w - 1 - b + h- 1 - i - (w - b - 1)
        comb2 %= MOD

    print(ans)


if __name__ == '__main__':
    main()
