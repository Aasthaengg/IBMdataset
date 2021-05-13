n = int(input())

def f(lst):
  res = 0
  ex = 0
  for a in lst:
    ex += a
    res += ex//2
    ex %= 2
  return res

A = []
ans = 0
for _ in range(n):
  a = int(input())
  if a%2:
    ans += a//2
    a = 1
  else:
    if a>2:
      ans += a//2-1
      a = 2

  if a!= 0:
    A.append(a)
  elif A:
    ans += max(f(A), f(A[::-1]))
    A = []
  else:
    continue
else:
  ans += max(f(A), f(A[::-1]))
print(ans)

