N, L = map(int, input().split())
a = list(map(int, input().split()))

idx = -1
for i in range(N - 1):
  if a[i] + a[i + 1] >= L:
    idx = i
    break

if idx == -1:
  print("Impossible")
else:
  print("Possible")
  for i in range(idx):
    print(i + 1)
  for i in range(N - 1, idx, -1):
    print(i)