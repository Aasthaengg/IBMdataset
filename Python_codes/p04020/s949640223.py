n=int(input())
carry=0
ans=0
for i in range(n):
  a=int(input())
  carrycopy=carry
  carry=(carry+a)%2
  ans+=(a+carrycopy)//2
  if a==0:
    carry=0
print(ans)