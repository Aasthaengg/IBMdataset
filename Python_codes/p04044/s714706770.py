n, l = map(int, input().split())
s = []
for i in range(n):
  a = input()
  s.append(a)

s = sorted(s)
print("".join(s))