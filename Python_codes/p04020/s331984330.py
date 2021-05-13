n=int(input())
c=0
am=0
for i in range(n):
  a=int(input())
  c+=(am+a)//2
  am=(am+a)%2
  if a==0:
    am=0
print(c)