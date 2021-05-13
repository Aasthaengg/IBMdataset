n, l = map(int, input().split())
a = list(input() for i in range(n))
ans = ''
for i in sorted(a):
  ans += i
print(ans)