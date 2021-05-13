N = int(input())
L = input().split(" ")
for i in range(0, len(L)):
  L[i] = int(L[i])
L.sort()

ans = 0
for i in range(0, len(L), 2):
  tmp = L[i]
  if tmp > L[i+1]:
    tmp = L[i+1]
  ans += tmp
print(ans)