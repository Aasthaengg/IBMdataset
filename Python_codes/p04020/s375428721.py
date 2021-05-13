n = int(input())
ans = 0
sum = 0
for _ in range(n):
  a = int(input())
  if a == 0:
    ans += sum//2
    sum = 0
    continue
  sum += a
ans += sum // 2
print(ans)