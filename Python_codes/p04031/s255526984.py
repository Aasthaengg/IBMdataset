n = int(input())
a = list(map(int, input().split()))
l = []
for i in range(min(a), max(a) + 1):
  c = 0
  for e in a:
    c += (e - i) ** 2
  l.append(c)
print(min(l))