N,L=map(int,input().split())
a=list(map(int,input().split()))

aa_max=-1
aa_i=-1
for i in range(N-1):
  if a[i]+a[i+1]>aa_max:
    aa_max=a[i]+a[i+1]
    aa_i=i
#print(aa_max,aa_i)

if aa_max<L:
  print("Impossible")
else:
  print("Possible")
  for i in range(aa_i):
    print(i+1)
  for i in range(N-2,aa_i-1,-1):
    print(i+1)