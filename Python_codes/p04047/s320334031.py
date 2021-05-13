n = int(input())
l = list(map(int,input().split()))
l.sort()
c = 0
for i in range(n):
  c += l[2*i]
print(c)