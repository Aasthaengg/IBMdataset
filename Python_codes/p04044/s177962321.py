a,b=input().split()
a=int(a)
b=int(b)
c=[input() for i in range(a)]
c.sort()
d=""
for k in range(a):
  d=d+c[k]
print(d)