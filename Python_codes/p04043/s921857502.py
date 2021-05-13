a=list(map(int,input().split()))

b=a[0]+a[1]+a[2]
c=a[2]-a[1]-a[0]

if b==17 and (c==-7 or c==-3):
  
  print('YES')

else:
  print('NO')
