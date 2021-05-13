n, l = map(int, input().split())
a = []
if n == 1:
  print(input())
  exit()
for i in range(n):
  a.append(input())
a.sort()
a = ''.join(a)
print(a)