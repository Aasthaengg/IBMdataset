K = 10 ** 9 + 7

def pow_K(x, n):
  if n == 0:
    return 1
  else:
    return (pow_K(x, n // 2) ** 2 * x ** (n % 2)) % K

H, W, A, B = map(int, input().split())

fact = [0 for i in range(H+W-1)]
fact[0] = 1
for i in range(H+W-2):
  fact[i + 1] = fact[i] * (i+1) % K
fact_inv = [0 for i in range(H+W-1)]
fact_inv[H+W-2] = pow_K(fact[H+W-2], K-2)
for i in range(H+W-2, 0, -1):
  fact_inv[i-1] = fact_inv[i] * i % K

r = 0
for i in range(B, W):
  r += ((fact[H-A-1+i] * fact_inv[H-A-1] %K)*fact_inv[i] % K) * ((fact[W-1-i+A-1] * fact_inv[W-1-i] %K) * fact_inv[A-1] % K) %K
  r %= K

print(r)


