n = int(input())
ans = 0
chk = 0
for i in range(n):
  a = int(input())
  p = chk+a
  ans += p//2
  if a > 0:
    chk = p%2
  else:
    chk = 0
print(ans)