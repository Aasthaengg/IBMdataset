n, l = map(int, input().split())
A = list(map(int, input().split()))
for i in range(n-1):
  if A[i]+A[i+1] >= l:
    f = i+1
    break
else:
  print("Impossible")
  exit()
print("Possible")
for i in range(1, f):
  print(i)
for i in range(n-1, f, -1):
  print(i)
print(f)