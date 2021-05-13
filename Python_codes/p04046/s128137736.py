import math
H, W, A, B = map(int, input().split())
p = 10 ** 9 + 7
F = [1 for i in range(H + W + 1)]
for i in range(1, H + W + 1):
  F[i] = F[i - 1] * i % p
def fac(a, b):
  a = F[a + b] * pow(F[a], p - 2, p) * pow(F[b], p - 2, p)
  return a % p
ans = 0
for h in range(H - A):
  ans += fac(h, B - 1) * fac(H - h - 1, W - B - 1) % p
print(ans % p)