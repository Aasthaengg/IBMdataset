n, = [int(v) for v in input().split()]
l = [int(v) for v in input().split()]

l.sort()

ans = 0
for i in range(n):
  ans += l[2 * i]
print(ans)