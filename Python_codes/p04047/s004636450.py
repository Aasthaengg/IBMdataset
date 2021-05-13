n = input()
a = sorted(list(map(int, input().split())))
ans = 0
for i in range(0, len(a), 2):
  ans += a[i]
print(ans)