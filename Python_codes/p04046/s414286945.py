h, w, a, b = map(int, input().split())
res = 0
kai = min(w - b, h - a)
mod = 10 ** 9 + 7

kaijo = [0] * (h + w + 1)
kaijo[0] = 1
for i in range(1, h + w + 1):
    kaijo[i] = (kaijo[i - 1] * i) % mod
gyaku = [0] * (h + w + 1)
gyaku[h + w] = pow(kaijo[h + w], mod - 2, mod)
for i in range(h + w, 0, -1):
    gyaku[i - 1] = (gyaku[i] * i) % mod


def conb(x, k):
    return (kaijo[x] * gyaku[k] * gyaku[x - k]) % mod


conb1 = conb(h - a - 1 + b, b)
conb2 = conb(a + w - b - 1, a)
combi = conb1 * conb2
res = combi

for i in range(1, kai):
    res += conb(h - a - 1 + b, b + i) * conb(a + w - b - 1, a + i)

res %= mod
print(int(res))
