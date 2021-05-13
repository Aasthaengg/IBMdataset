n = int(input())
c = 0
ans = 0
for _ in range(n):
  t = int(input())
  if t == 0:
    ans += c//2
    c = 0
  c += t
ans += c//2
print(ans)