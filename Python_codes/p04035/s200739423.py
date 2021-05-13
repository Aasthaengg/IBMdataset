n,k = map(int,input().split())
a = list(map(int,input().split()))
for i in range(n-1):
  if a[i]+a[i+1] >= k:
    print("Possible")
    x = i
    break
else:
  print("Impossible")
  exit()
if x == 0:
  print(*list(range(1,n))[::-1],sep="\n")
else:
  ans = list(range(1,n))
  ans[x:] = ans[n-1:x-1:-1]
  print(*ans,sep="\n")