n, l = [int(v) for v in input().split()]
a_s = [int(v) for v in input().split()]

piv = -1
b_s = []
for i in range(n - 1):
  a2 = a_s[i] + a_s[i + 1]
  b_s.append(a2)
  if a2 >= l:
    piv = i

if piv == -1:
  print("Impossible")
else:
  print("Possible")
  for i in range(piv):
    print(i + 1)
  for i in range(n-2, piv - 1, -1):
    print(i + 1)