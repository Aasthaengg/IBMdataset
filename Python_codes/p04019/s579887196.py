s = input()

L = [['W', 'E'], ['S', 'N']]

for l in L:
  if l[0] in s:
    if l[1] not in s:
      print("No")
      exit(0)
  if l[1] in s:
    if l[0] not in s:
      print("No")
      exit(0)

print("Yes")