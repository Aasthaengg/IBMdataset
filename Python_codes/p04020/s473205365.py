N, *A = map(int, open(0).read().split())
ls = []
s = 0
ans = 0
for c in A:
  if c==0:
    ans += s//2
    s = 0
  else:
    s += c
ans += s//2
print(ans)