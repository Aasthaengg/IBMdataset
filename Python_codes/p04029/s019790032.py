n = int(input())
k = 0
if 1 <= n <= 100:
  for i in range(n):
    k += i + 1
print(k)