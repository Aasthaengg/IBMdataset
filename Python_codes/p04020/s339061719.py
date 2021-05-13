N = int(input())
ans = 0
tmp = 0
i = 0
while i < N:
  a = int(input())
  if a == 0:
    ans += tmp //2
    tmp = 0
  else:
    tmp += a
  i += 1
ans += tmp // 2
print(ans)