N = int(input())
L = list(map(int, input().split()))
vlist = []
ans = 0

for i in range(N):
  a = max(L)
  L.remove(a)
  b = max(L)
  L.remove(b)
  if a < b:
    vlist.append(a)
  else:
    vlist.append(b)

for i in range(N):
  ans += vlist[i]
  
print(ans)