n = int(input())
a = []
cnt = 0
for i in range(n):
  a.append(int(input()))
stack = -1
for i in range(n):
  if i+1 - stack <= 1 and a[i] > 0:
    cnt += 1
    a[i] -= 1
    stack = -1
  cnt += a[i] // 2
  if a[i] % 2 == 1:
    stack = i+1
  else:
    stack = -1
print(cnt)