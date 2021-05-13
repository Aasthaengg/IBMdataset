H, W, A, B = list(map(int, input().split()))
p = 1000000007

fac = [1] * (H + W + 1)
x = 1
for i in range(1, H + W + 1):
    x *= i
    x %= p
    fac[i] = x

ifac = [1] * (H + W + 1)
x = fac[H + W]
q = p - 2

while q > 0:
    if q & 1:
        ifac[H + W] *= x % p
    x *= x % p
    q >>= 1

for i in range(H + W - 1, 0, -1):
    ifac[i] = ifac[i + 1] * (i + 1) % p

def com(a, b):
    return (fac[a] * ifac[b] * ifac[a-b]) % p

ans = 0

for i in range(H-A):
    ans += com(B+i-1, i) * com(W-B+H-i-2, H-i-1)
    ans %= p

print(ans)
