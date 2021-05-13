n = int(input())
a = []
for i in range(n):
  a.append(int(input()))
res = 0
for i in range(n):
  res += a[i] // 2
  if a[i] % 2 == 1:
    if i != n-1:
      if a[i+1] != 0:
        res += 1
        a[i+1] -= 1
  
print(res)