N, L = map(int, input().split())
As = list(map(int, input().split()))
n = -1
for i in range(1, N):
  if As[i-1]+As[i] >= L:
    n = i
    break
#print(n)
if n < 0:
  print("Impossible")
  exit()
print("Possible")
for i in range(n-1):
  print(i+1)
for i in reversed(range(n, N)):
  print(i)
