n,l=map(int,input().split())
a=list(map(int,input().split()))
m=0
x=0
for i in range(n-1):
  if((a[i]+a[i+1])>=m):
    m=a[i]+a[i+1]
    x=i
if(m<l):
  print("Impossible")
else:
  print("Possible")
  for j in range(x):
    print(j+1)
  for k in range(n-1,x+1,-1):
    print(k)
  print(x+1)