n,l = input().split()
S = []
for i in range(int(n)):
  S.append(input())
S.sort()
str = ''
for s in S:
  str += s
print(str)