n=int(input())
x=0
z=0
for i in range(n):
  t=int(input())
  if t:
    x+=t
  else:
    z+=x//2
    x=0
print(z+x//2)