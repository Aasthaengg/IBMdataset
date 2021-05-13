h, w, a, b = map(int, input().split(" "))
div = 10 ** 9 + 7
size = h + w - 1

fact = [0] * size
inverse = [0] * size
inv_calced = [0] * size
fact[:2] = [1, 1]
inverse[:2] = [1, 1]
inv_calced[:2] = [0, 1]

for i in range(2, size):
  fact[i] = fact[i - 1] * i % div
  inv_calced[i] = -inv_calced[div % i] * (div // i) % div
  inverse[i] = inverse[i - 1] * inv_calced[i] % div
  
result = 0
for x in range(b, w):
  y = h - a - 1
  temp_1 = (fact[x+y] * inverse[x] % div) * inverse[y] % div
  temp_2 = (fact[h+w-x-y-3] * inverse[w-x-1] % div) * inverse[h-y-2] % div
  result += ((temp_1 % div) * (temp_2 % div)) % div

print(result % div)