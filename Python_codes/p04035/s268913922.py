N, L = map(int, input().split())
A = list(map(int, input().split()))
l = max_2 = A[0] + A[1]
idx = 0
for i in range(N-2):
  l += A[i+2] - A[i]
  if l > max_2:
    max_2 = l
    idx = i + 1

if max_2 < L:
  print('Impossible')
else:
  print('Possible')
  for i in range(1, idx + 1):
    print(i)
  for i in range(N-1, idx, -1):
    print(i)