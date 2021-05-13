N,L=map(int,input().split())
a=[int(i) for i in input().split()]
Longest_pair=0
p=0
for i in range(N-1):
  if a[i]+a[i+1]>Longest_pair:
    Longest_pair=a[i]+a[i+1]
    p=i+1
if Longest_pair<L:
  print("Impossible")
  exit()
else:
  print("Possible")
for i in range(1,p):
  print(i)
for i in range(p+1,N)[::-1]:
  print(i)
print(p)
