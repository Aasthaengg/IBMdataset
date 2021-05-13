import math
h, w, a, b = [int(i) for i in input().split()]

MOD = 10**9 + 7
N = h + w

fact = [1]*(N+1)
rfact = [1]*(N+1)
r = 1
for i in range(1, N+1):
  fact[i] = r = r * i % MOD
rfact[N] = r = pow(fact[N], MOD-2, MOD)
for i in range(N, 0, -1):
  rfact[i-1] = r = r * i % MOD

def comb(n, k):
  return fact[n] * rfact[k] * rfact[n-k] % MOD

tmp = []
for i in range(b, w):
    tmp.append(comb(i+h-a-1, i))

ans = 0
cnt = 0
for i in range(w-b-1, -1, -1):
    t = comb(i + a - 1, a - 1)
    ans += t * tmp[cnt]
    cnt += 1
print(ans%MOD)