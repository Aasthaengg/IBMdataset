h, w, a, b = map(int, input().split())

modulo = 10 ** 9 + 7

factorials = [1]
for i in range(1, h + w + 1):
    factorials.append((factorials[-1] * i) % modulo)


inverses = []
for f in factorials:
    inverses.append(pow(f, modulo - 2, modulo))

def cnk(n, k):
    return (factorials[n] * inverses[k] * inverses[n - k]) % modulo


line_before = [0] * w

for j in range(b, w):
    line_before[j] = cnk(h - a - 1 + j, h - a - 1)


s = 0
for j in range(b, w):
    s += cnk(a + w - j - 2, a - 1) * line_before[j]
    s %= modulo

print(s)
