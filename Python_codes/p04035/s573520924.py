n,l=map(int,input().split())
a=list(map(int,input().split()))
f=True
for i in range(n-1):
  if a[i]+a[i+1]>=l:
    print("Possible")
    print("\n".join([str(j) for j in range(1,i+1)]+[str(j) for j in range(n-1,i+1,-1)]+[str(i+1)]))
    f=False
    break
if f:
  print("Impossible")
