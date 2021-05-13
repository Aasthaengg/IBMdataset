N = int(input())
A = [int(i) for i in input().split()]

ans = 200**2 * 100
for y in range(-100, 101):
  a = 0
  for x in A:
    a += (x-y)**2
  ans = min(ans, a)

print(ans)


