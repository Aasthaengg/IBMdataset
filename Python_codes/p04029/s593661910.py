n = int(input())

if n % 2 == 0:
  ans = (n+1) * n/2
else:
  ans = (n+1) * (n // 2) + (n // 2 + 1)

print(int(ans))