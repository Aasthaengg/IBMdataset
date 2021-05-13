n=int(input())
c=0
cu=0
for i in range(n):
  a=int(input())
  if cu and a:
    a-=1
    c+=1
  c+=a//2
  cu=a%2
print(c)