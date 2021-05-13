H, W, A, B = map(int, input().split())
p = 10 ** 9 + 7
F = [1 for i in range(H + W + 1)]
for i in range(1, H + W + 1):
  F[i] = F[i - 1] * i % p
Fi = [pow(f, p - 2, p) for f in F]
def fac(a, b):
  a = F[a + b] * Fi[a] * Fi[b]
  return a % p
if H - A < B:
  ans = 0
  for h in range(H - A):
    ans += fac(h, B - 1) * fac(H - h - 1, W - B - 1) % p
else:
  ans = fac(H - 1, W- 1)
  for w in range(B):
    ans -= fac(H - A - 1, w) * fac(A - 1, W - w - 1) % p
print(ans % p)