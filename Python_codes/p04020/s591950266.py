n = int(input())
s = 0
z = 0
for _ in range(n):
  ai = int(input())
  s += (z+ai)//2
  if z == 1 and z+ai >= 3:
    z = (ai+1)%2
  else:
    z = ai%2
print(s)