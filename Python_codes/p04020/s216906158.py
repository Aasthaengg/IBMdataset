N = int(input())
l = []
for i in range(N):
  l.append(int(input()))
  
ans = 0
for i in range(N):
  ans += l[i] // 2
  l[i] = l[i] % 2
  if (i<N-1) and (l[i]==1) and (l[i+1]>0):
    ans += 1
    l[i] = 0
    l[i+1] -= 1
print(ans)