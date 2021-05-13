def modpow(a, n, mod):
  res = 1
  while n > 0:
    if (n & 1):
      res = res * a % mod
    a = a * a % mod
    n >>= 1
  return res

DIV = 10**9 + 7
h, w, a, b = map(int, input().split())
ans = 0
#最大h+w!までの元と逆元の階乗テーブルを求めておく
#逆元をFermatの小定理により計算
#p-2乗は二分累乗法にて高速に計算可能
table = [1 for i in range(h + w + 1)]
inv_table = [1 for i in range(h + w + 1)]
temp = 1
for i in range(1, h + w + 1):
  temp = temp * i % DIV
  table[i] = temp
  inv_table[i] = modpow(temp, DIV - 2, DIV)

for i in range(w - b):
  n1 = table[h + i + b - a - 1] * inv_table[b + i] * inv_table[h - a - 1] % DIV
  n2 = table[w + a - b - 2 - i] * inv_table[a - 1] * inv_table[w - b - 1 - i] % DIV
  ans += n1 * n2 % DIV
ans = int(ans)
print(ans%DIV)