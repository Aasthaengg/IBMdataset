n = int(input())
A = [int(input()) for _ in range(n)]
ans = 0
pre = 0
for a in A:
  d, m = divmod(pre + a, 2)
  ans += d
  if m == 1 and a > 0: pre = 1
  else: pre = 0
print(ans)