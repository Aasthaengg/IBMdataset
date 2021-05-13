N = int(input())
ans = 0
prev = 0
for i in range(N):
  a = int(input())
  if prev == 1 and a >= 1:
    ans += 1
    a -= 1
  ans += a // 2
  prev = a % 2
print(ans)