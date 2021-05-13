M = 1000000007
h, w, a, b = list(map(int, input().split()))


def inv(k):
    return pow(k, M - 2, M)


def comb(n, k):
    if n < k:
        return 0
    elif k == 0:
        return 1
    else:
        r = 1
        for i in range(k):
            r = (r * ((n - i) * inv(k - i)) % M) % M
        return r


ans = comb(h + w - 2, h - 1)

if a == 1 and b == 1:
    ans -= 1
elif a == 1:
    ans -= comb(h + b - 2, h - 1)
elif b == 1:
    ans -= comb(w + a - 2, w - 1)
else:

    memo = [1] * b
    for i in range(1, b):
        memo[i] = (memo[i - 1] * (h - a + i) * inv(i)) % M

    memo2 = [0] * b
    height = a - 1
    width = w - b
    memo2[b - 1] = comb(height + width, height)
    for i in range(1, b):
        memo2[b - i - 1] = (memo2[b - i] * (height + width + i) * inv(width + i)) % M

    ans -= memo[0] * memo2[0]
    ans %= M
    for i in range(1, b):
        ans -= (memo[i] - memo[i - 1]) * memo2[i]
        ans %= M

print(ans % M)
