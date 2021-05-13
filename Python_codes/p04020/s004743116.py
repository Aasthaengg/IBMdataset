n = int(input())
ans = 0
bef = 0
for _ in range(n):
  a = int(input())
  if a == 0:
    bef = 0
    continue
  ans += (a + bef) // 2
  if (a + bef) % 2 == 1:
    bef = 1
  else:
    bef = 0
print(ans)